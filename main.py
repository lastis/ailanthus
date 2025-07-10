import time
from dataclasses import dataclass

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


class TreeSimulation:
    """Console-based tree simulation using ECS pattern."""

    def __init__(self):
        # Clear any existing esper world data
        esper.clear_database()

        # Add the energy processing system
        self.energy_processor = EnergyProcessingSystem()
        esper.add_processor(self.energy_processor)

        # Create a tree entity with energy component
        self.tree_entity = esper.create_entity()
        esper.add_component(self.tree_entity, EnergyComponent(energy=0))

        print(f"Created tree entity {self.tree_entity} with initial energy")

    def run_simulation(self, cycles: int = 10):
        """Run the tree simulation for a specified number of cycles."""
        print(f"\nStarting tree simulation for {cycles} cycles...")
        print("=" * 50)

        for cycle in range(cycles):
            print(f"\nCycle {cycle + 1}:")
            # Process all systems in the ECS world
            esper.process()

            # Get current tree energy for display
            energy_comp = esper.component_for_entity(self.tree_entity, EnergyComponent)

            # Simple ASCII representation of tree growth
            tree_visual = self.get_tree_visual(energy_comp.energy)
            print(tree_visual)

            # Wait a bit between cycles for visual effect
            time.sleep(0.5)

    def get_tree_visual(self, energy: int) -> str:
        """Generate ASCII art representation of tree based on energy."""
        # Tree canopy size based on energy
        canopy_size = min(energy // 2, 5)  # Max size of 5

        tree_lines = []

        # Tree canopy - gets bigger with more energy
        for i in range(canopy_size + 1):
            spaces = " " * (5 - i)
            leaves = "🌿" * (i + 1)
            tree_lines.append(f"{spaces}{leaves}")

        # Tree trunk
        trunk_spaces = " " * 4
        tree_lines.append(f"{trunk_spaces}🟫")
        tree_lines.append(f"{trunk_spaces}🟫")

        return "\n".join(tree_lines)


def main():
    """Main entry point for the tree simulation."""
    # Create and run the simulation
    simulation = TreeSimulation()
    simulation.run_simulation(cycles=15)


if __name__ == "__main__":
    main()
