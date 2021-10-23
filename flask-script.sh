#!/bin/bash

# Script to run two web apps on the same host (for debugging pruposes)
# This script can be run only if the venv is enabled
# TO ADD: condition to check if venv is enabled, and enable if not

# Still not running in parallel

# Backend Application
export FLASK_APP=./backend/backend-app.py
flask run --host 0.0.0.0 --port 5000

export FLASK_APP=./backend/backend-app.py
flask run --host 0.0.0.0 --port 5002

# Frontend Application
export FLASK_APP=./frontend/frontend-app.py
flask run --host 0.0.0.0 --port 5001