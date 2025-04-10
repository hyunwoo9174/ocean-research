# Use a base image
FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    LANGUAGE=C.UTF-8 \

# Set timezone and update system
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    wget \
    git \
    gfortran \
    octave \
    gnuplot \
    texlive-science && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Add user and configure environment
RUN useradd -ms /bin/bash user && \
    echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    echo "user:user" | chpasswd && \
    mkdir -p /home/user/bin /home/user/.local/bin && \
    echo 'export PATH=$PATH:/home/user/bin:/home/user/.local/bin' >> /home/user/.bashrc && \
    echo 'export PATH=$PATH:/home/user/bin:/home/user/.local/bin' >> /home/user/.bash_profile

# Switch to user
USER user

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Default command
CMD ["bash"]

