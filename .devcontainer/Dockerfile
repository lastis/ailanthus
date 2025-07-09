FROM mcr.microsoft.com/devcontainers/base:debian

# Install Taskfile
RUN sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv /root/.local/bin/uv /usr/local/bin/uv
