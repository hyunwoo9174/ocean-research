# Use a base image
FROM ubuntu:latest

# Update and install system-wide programs
RUN apt-get update && apt-get install -y \
    gfortran \
    octave \
    gnuplot \
    texlive-science \
    wget \
    vim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Default command
CMD ["bash"]

