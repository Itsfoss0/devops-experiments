#!/usr/bin/env bash

# Activate the virtual environment

if [[ -d  "/home/$USER/virtualenenvs/dev/bin/" ]]; then
    source "/home/$USER/virtualenenvs/dev/bin/activate";
else
    echo "ENV not found. Creating it now..."
    python -m venv /home/$USER/virtualenenvs/dev;
    source "/home/$USER/virtualenenvs/dev/bin/activate";
fi
