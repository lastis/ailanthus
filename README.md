# Ailanthus - Tree Growth Simulation

A Python-based tree growth simulation using the Arcade game library and Esper ECS (Entity Component System) pattern.

## Features

- **Visual Tree Growth**: Watch a tree grow dynamically based on its energy level
- **ECS Architecture**: Clean separation using Entity Component System pattern
- **Graphics Support**: Full OpenGL support in dev containers
- **Headless Mode**: Option to run without graphics (for future console implementation)

## Quick Start

1. **Run the simulation**:
   ```bash
   task run
   # or just: task (runs the default task)
   ```

2. **Test graphics support**:
   ```bash
   task test-graphics
   ```

3. **Install dependencies** (if needed):
   ```bash
   task install
   ```

## Available Commands

- `task run` - Run the simulation with graphics (default)
- `task run-headless` - Run without graphics (console mode)
- `task test-graphics` - Test OpenGL and graphics support
- `task install` - Install all dependencies

## Graphics in Dev Container

This project is configured to work with OpenGL graphics in a dev container environment:

- **Virtual Display**: Uses Xvfb for headless OpenGL rendering
- **Libraries**: All necessary OpenGL, X11, and font libraries are installed
- **Auto-setup**: The `start_display.sh` script automatically starts the virtual display

## How It Works

### ECS Components
- **EnergyComponent**: Stores the tree's energy value

### ECS Systems
- **EnergyProcessingSystem**: Increases tree energy over time

### Visual Elements
- **Tree Trunk**: Grows taller as energy increases
- **Tree Canopy**: Expands with multiple overlapping circles
- **Detailed Leaves**: Added when energy exceeds threshold
- **Energy Display**: Shows current energy level in real-time

### Game Flow
1. Tree starts with 0 energy
2. Energy increases by 1 every second
3. Visual representation grows accordingly:
   - Trunk height: 50 + energy × 5 pixels (max 150)
   - Canopy radius: 20 + energy × 3 pixels (max 80)
   - Extra leaves appear when energy > 5

## Development

The project uses modern Python tooling:
- **Python 3.13+** 
- **uv** for package management
- **Taskfile** for command runner
- **Dev Container** with pre-configured environment

### Dependencies
- `arcade>=3.3.2` - 2D game development
- `esper>=3.4` - Entity Component System
- `PyOpenGL>=3.1.7` - OpenGL bindings

## Architecture Notes

- Follows ECS patterns for clean separation of concerns
- Uses minimal code with efficient list comprehensions
- Organized in logical paragraphs with explanatory comments
- Leverages NumPy for potential vectorized operations
- Modern Python features and type hints throughout
