#!/bin/bash
# Check if user is root
if [ "$(id -u)" != "0" ]; then
  echo "Error: You must be root to run this script, please use root to install"
  exit 1
fi
