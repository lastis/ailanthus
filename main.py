import argparse
import time
from dataclasses import dataclass

import arcade
import esper


# Component that represents a tree's energy state
@dataclass
class EnergyComponent:
    """Component storing the energy value for a tree entity."""

    energy: int = 0


# System that processes energy increase for trees
class EnergyProcessingSystem(esper.Processor):
    """System that increases energy for all entities with EnergyComponent."""

    def process(self, dt: float = 0):
        # Process all entities that have an EnergyComponent
        for entity, energy_comp in esper.get_component(EnergyComponent):
            energy_comp.energy += 1
            print(f"Tree entity {entity}: energy = {energy_comp.energy}")


class TreeGame(arcade.Window):
    """Arcade-based tree simulation using ECS pattern."""

    def __init__(self):
        # Initialize the arcade window
        super().__init__(800, 600, "Ailanthus Tree Simulation")
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Clear any existing esper world data
        esper.clear_database()

        # Add the energy processing system
        self.energy_processor = EnergyProcessingSystem()
        esper.add_processor(self.energy_processor)

        # Create a tree entity with energy component
        self.tree_entity = esper.create_entity()
        esper.add_component(self.tree_entity, EnergyComponent(energy=0))

        # Game timing
        self.last_update = time.time()
        self.update_interval = 1.0  # Update every 1 second

    def on_update(self, delta_time: float):
        """Update game state."""
        # Check if enough time has passed to update the tree
        current_time = time.time()
        if current_time - self.last_update >= self.update_interval:
            # Process all systems in the ECS world
            esper.process()
            self.last_update = current_time

    def on_draw(self):
        """Render the game."""
        # Clear the screen
        self.clear()

        # Get current tree energy
        energy_comp = esper.component_for_entity(self.tree_entity, EnergyComponent)

        # Draw ground using lbwh (left, bottom, width, height)
        arcade.draw_lbwh_rectangle_filled(0, 0, self.width, 100, arcade.color.BROWN)

        # Draw tree based on energy level
        self.draw_tree(energy_comp.energy)

        # Draw energy text
        arcade.draw_text(f"Tree Energy: {energy_comp.energy}", 10, self.height - 30, arcade.color.WHITE, 20)

    def draw_tree(self, energy: int):
        """Draw the tree based on its energy level."""
        # Tree position
        tree_x = self.width // 2
        ground_y = 100

        # Tree trunk - grows taller with energy
        trunk_width = 20
        trunk_height = min(50 + energy * 5, 150)  # Max height of 150

        # Create rect for trunk and draw it
        trunk_rect = arcade.XYWH(tree_x, ground_y + trunk_height // 2, trunk_width, trunk_height)
        arcade.draw_rect_filled(trunk_rect, arcade.color.DARK_BROWN)

        # Tree canopy - grows bigger with energy
        canopy_radius = min(20 + energy * 3, 80)  # Max radius of 80
        canopy_y = ground_y + trunk_height + canopy_radius // 2

        # Multiple circles for fuller canopy effect
        for i in range(3):
            offset_x = (i - 1) * canopy_radius // 3
            offset_y = (i - 1) * canopy_radius // 6

            arcade.draw_circle_filled(
                tree_x + offset_x, canopy_y + offset_y, canopy_radius // (1 + i * 0.2), arcade.color.GREEN
            )

        # Add some leaves/branches for detail when energy is high
        if energy > 5:
            for i in range(min(energy // 2, 8)):
                leaf_x = tree_x + (i - 4) * 15
                leaf_y = canopy_y + (i % 3 - 1) * 20
                arcade.draw_circle_filled(leaf_x, leaf_y, 8, arcade.color.FOREST_GREEN)


def main():
    """Main entry point for the tree simulation game."""
    parser = argparse.ArgumentParser(description="Ailanthus Tree Simulation")
    parser.add_argument("--no-graphics", action="store_true", help="Run without graphics (console mode only)")
    args = parser.parse_args()

    if args.no_graphics:
        print("Running in console mode...")
        # TODO: Add console-only simulation later
        print("Console mode not implemented yet. Use graphics mode.")
        return

    # Create and run the arcade game
    game = TreeGame()
    arcade.run()


if __name__ == "__main__":
    main()
