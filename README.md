# Ailanthus - Tree Growth Simulation

A Python-based tree growth simulation using the Arcade game library and Esper ECS (Entity Component System) pattern.

## Features

- **Visual Tree Growth**: Watch a tree grow dynamically based on its energy level
- **ECS Architecture**: Clean separation using Entity Component System pattern
- **Graphics Support**: Full OpenGL support in dev containers
- **Headless Mode**: Option to run without graphics (for future console implementation)

## Development Environment

- **Python 3.13.3** with uv package management
- **Taskfile** for command runner
- **Dev Container** with Debian-based environment
- **Key Dependencies**: arcade, esper, numpy

## Quick Start

1. **Run the simulation**:

   ```bash
   task run
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
- `task test-graphics` - Test graphics window support
- `task setup-xquartz` - Run XQuartz setup script (macOS host only)
- `task install` - Install all dependencies

## Graphics Setup

This project displays real graphics windows using XQuartz on macOS:

### Initial Setup (macOS)

1. **Install XQuartz** (if not already installed):

   ```bash
   brew install --cask xquartz
   ```

2. **Run the setup script** (on macOS host, not in container):

   ```bash
   task setup-xquartz
   ```

3. **Rebuild the dev container** in VS Code:
   - `Cmd+Shift+P` → "Dev Containers: Rebuild Container"

### Manual XQuartz Configuration

If automatic setup doesn't work:

1. **Start XQuartz** and open Preferences
2. **Security tab**: Check "Allow connections from network clients"
3. **Terminal**: Run `xhost +localhost`

### Graphics Libraries

- **OpenGL Support**: Full hardware-accelerated rendering
- **X11 Integration**: Direct window display on macOS desktop
- **Testing Tools**: Built-in graphics validation

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

The project uses modern Python tooling and follows ECS patterns:

- **Python 3.13+**
- **uv** for package management
- **Taskfile** for command runner
- **Dev Container** with pre-configured environment

### Key Libraries

- `arcade` - 2D game development
- `esper` - Entity Component System
- `PyOpenGL` - OpenGL bindings
- `numpy` - Numerical computing

### Development Guidelines

- Use ECS patterns with clear entity/component/system separation
- Write minimal code with list comprehensions when appropriate
- Follow PEP 8 with type hints and descriptive names
- Write code in paragraphs with the first comment explaining the purpose of each section (newline signifies a new paragraph)
- Prefer vectorized NumPy operations over loops
