# Copilot Instructions for Ailanthus

## Project Overview

This is a Python project called "ailanthus" that uses the Arcade game library and
Esper ECS (Entity Component System) library. The project is set up with modern Python tooling including uv for package management and runs in a dev container environment.

## Development Environment

- Python 3.13.3
- Package manager: uv
- Command runner: Taskfile (task command)
- Dev container: Debian-based with pre-installed tools

## Project Structure

- `.venv/` - Virtual environment directory
- `src/ailanthus` - Source code for the Ailanthus game
- `main.py` - Entry point of the application
- `pyproject.toml` - Project configuration and dependencies
- `Taskfile.yml` - Task definitions for common operations
- `.python-version` - Python version specification
- `.devcontainer/` - Dev container configuration

## Important Dependencies

- **arcade** - 2D game development library
- **esper** - Entity Component System library
- **numpy** - Numerical computing library

## Coding Standards & Preferences

### General Coding Guidelines

- Write minimal code and prefer list comprehensions when appropriate.
- Write code in paragraphs such with the first comment explaining the purpose of each section.
  Newline signifies a new paragraph. Comments can be used multiple times in a paragraph.
- Prefer vectorised operations with NumPy instead of loops when appropriate.
- Follow PEP 8 style guidelines.
- Use type hints for function parameters and return types.
- Prefer f-strings for string formatting.
- Use descriptive variable and function names.
- Add docstrings for classes and functions.

### Game Development Patterns

- Use Entity Component System (ECS) patterns with Esper
- Organize game entities, components, and systems clearly
- Follow Arcade library conventions for game structure
- Separate game logic from rendering code

### Code Organization

- Keep related functionality grouped together
- Use classes for complex game objects
- Create separate modules for different game systems
- Follow single responsibility principle

### Error Handling

- Use appropriate exception handling
- Provide meaningful error messages
- Handle game-specific errors gracefully

### Performance Considerations

- Be mindful of game loop performance
- Use efficient data structures for game entities
- Profile code when dealing with many entities

## Task Commands

- `task install` - Install dependencies with uv sync
- Use `uv` commands for package management
- Run Python scripts with `uv run main.py`

## Suggestions for Code Generation

When generating code for this project:

1. Write minimal code and prefer list comprehensions when appropriate.
2. Write code in paragraphs such with the first comment explaining the purpose of each section.
Newline signifies a new paragraph. Comments can be used multiple times in a paragraph.
3. Prefer vectorised operations with NumPy instead of loops when appropriate.
4. Consider ECS patterns when creating game entities
5. Use Arcade's built-in classes and methods appropriately
6. Structure code for a game development workflow
7. Consider game loop and event handling patterns
8. Use modern Python features and syntax
