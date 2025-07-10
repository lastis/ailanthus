#!/usr/bin/env python3
"""
Simple test to verify OpenGL support in the dev container.
"""

import sys


def test_opengl():
    """Test if OpenGL libraries are available."""
    try:
        import OpenGL.GL as gl

        print("✓ OpenGL Python bindings available")
        return True
    except ImportError as e:
        print(f"✗ OpenGL Python bindings not available: {e}")
        return False


def test_arcade():
    """Test if Arcade can initialize without errors."""
    try:
        import arcade

        print("✓ Arcade library available")

        # Try to create a minimal window (this will test OpenGL)
        window = arcade.Window(100, 100, "Test", visible=False)
        window.close()
        print("✓ Arcade window creation successful")
        return True
    except Exception as e:
        print(f"✗ Arcade initialization failed: {e}")
        return False


def main():
    """Run graphics tests."""
    print("Testing graphics support...")

    opengl_ok = test_opengl()
    arcade_ok = test_arcade()

    if opengl_ok and arcade_ok:
        print("\n✓ All graphics tests passed! Ready to run the tree simulation.")
        return 0
    else:
        print("\n✗ Some graphics tests failed. Check the setup.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
