#!/bin/bash
set -e
echo "Starting Cybersecurity Threat Intelligence Hub..."
uvicorn app:app --host 0.0.0.0 --port 9146 --workers 1
