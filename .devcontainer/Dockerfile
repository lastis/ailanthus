FROM mcr.microsoft.com/devcontainers/base:debian

# Install system dependencies for OpenGL and graphics
RUN apt-get update && apt-get install -y \
    # OpenGL libraries
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    libglapi-mesa \
    libglu1-mesa \
    # X11 libraries
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxtst6 \
    libxi6 \
    libxrandr2 \
    libxss1 \
    libxinerama1 \
    libxcursor1 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    # X11 client applications for testing
    x11-apps \
    xauth \
    # Audio support (optional for games)
    libasound2-dev \
    pulseaudio \
    # Clean up
    && rm -rf /var/lib/apt/lists/*

# Install Taskfile
RUN sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv /root/.local/bin/uv /usr/local/bin/uv

# Set up environment variables for OpenGL
ENV DISPLAY=host.docker.internal:0
ENV LIBGL_ALWAYS_INDIRECT=1
