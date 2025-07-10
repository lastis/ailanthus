#!/bin/bash
# Start virtual display for graphics support in headless environment

# Check if Xvfb is already running
if ! pgrep -x "Xvfb" > /dev/null; then
    echo "Starting virtual display..."
    Xvfb :99 -screen 0 1024x768x24 -ac +extension GLX +render -noreset &
    sleep 2
    echo "Virtual display started on :99"
else
    echo "Virtual display already running"
fi

# Set display environment
export DISPLAY=:99

# Run the provided command
exec "$@"
