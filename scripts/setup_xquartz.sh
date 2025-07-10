#!/bin/bash
# Setup script for XQuartz on macOS to work with dev container
# Run this script on your macOS host machine

echo "=== XQuartz Setup for Ailanthus Tree Simulation ==="
echo

# Check if XQuartz is installed
if ! command -v xquartz &> /dev/null; then
    echo "❌ XQuartz is not installed or not in PATH"
    echo "Please install XQuartz from https://www.xquartz.org/"
    echo "Or run: brew install --cask xquartz"
    exit 1
fi

echo "✅ XQuartz is installed"

# Check if XQuartz is running
if ! pgrep -x "Xquartz" > /dev/null; then
    echo "🚀 Starting XQuartz..."
    open -a XQuartz
    echo "Please wait for XQuartz to start completely..."
    sleep 3
else
    echo "✅ XQuartz is already running"
fi

# Configure XQuartz for network connections
echo "🔧 Configuring XQuartz for Docker connections..."
defaults write org.xquartz.X11 enable_iglx -bool true
defaults write org.xquartz.X11 nolisten_tcp -bool false
defaults write org.xquartz.X11 no_auth -bool false

echo "⚠️  You may need to restart XQuartz for settings to take effect"
echo "⚠️  In XQuartz preferences, make sure 'Allow connections from network clients' is checked"

# Allow connections from Docker
echo "🔐 Allowing X11 connections from Docker..."
xhost +localhost

echo
echo "=== Setup Complete ==="
echo "Your DISPLAY should be set to: host.docker.internal:0"
echo "Run 'task test-graphics-real' in your dev container to test"
echo
echo "If you get permission errors, try:"
echo "  xhost +localhost"
echo "  xhost +host.docker.internal"
