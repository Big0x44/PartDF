#!/bin/bash
# This script installs the PartDF tool on debian based systems.
# It downloads the script file from a GitHub and installs it to /usr/local/bin.
#
# Usage:
#   curl -sSL https://raw.githubusercontent.com/Big0x44/PartDF/refs/heads/main/install.sh | sudo sh

# Ensure the script is running as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root. Please run with sudo."
    exit 1
fi

# Check for required commands: python3, pip3, and curl
if ! command -v python3 >/dev/null 2>&1; then
    echo "python3 is not installed. Installing python..."
    apt update && apt install -y python3
fi

if ! command -v pip3 >/dev/null 2>&1; then
    echo "pip3 is not installed. Installing pip3..."
    apt update && apt install -y python3-pip
fi

if ! command -v curl >/dev/null 2>&1; then
    echo "curl is not installed. Installing curl..."
    apt update && apt install -y curl
fi

# Install the required Python package (pypdf)
echo "Installing pypdf..."
pip3 install pypdf

# URL of the partdf.py script in your GitHub repository
REPO_URL="https://raw.githubusercontent.com/Big0x44/PartDF/refs/heads/main/partdf.py"

# Download partdf.py to a temporary location
TMP_SCRIPT="/tmp/partdf.py"
echo "Downloading partdf.py from $REPO_URL..."
curl -sSL "$REPO_URL" -o "$TMP_SCRIPT"

if [ ! -s "$TMP_SCRIPT" ]; then
    echo "Failed to download partdf.py. Please check the URL and try again."
    exit 1
fi

# Set destination for the executable (must be in your PATH)
DESTINATION="/usr/local/bin/partdf"

echo "Installing tool to $DESTINATION..."
cp "$TMP_SCRIPT" "$DESTINATION"
chmod +x "$DESTINATION"

# Clean up temporary file
rm "$TMP_SCRIPT"

echo "Installation complete. You can now run the tool using:"
echo "  partdf -f file1.pdf file2.pdf -o merged_output.pdf"
