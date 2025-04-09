# Use a base image
FROM ubuntu:latest

# Update and install system-wide programs
RUN apt-get update && apt-get install -y \
    gfortran \
    texlive-science \
    octave \
    wget

# Install Miniforge for Python and Conda
RUN wget https://github.com/conda-forge/miniforge/releases/download/Miniforge3-Linux-x86_64.sh -O miniforge.sh && \
    bash miniforge.sh -b -p /opt/conda && \
    rm miniforge.sh && \
    /opt/conda/bin/conda init && \
    /opt/conda/bin/conda install -y -c conda-forge numpy scipy matplotlib

# Add Conda to PATH
ENV PATH="/opt/conda/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Default command
CMD ["bash"]

