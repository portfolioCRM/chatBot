#!/bin/bash

# Check if gunicorn is running before restart
echo "Checking if gunicorn is running..."
if pgrep gunicorn > /dev/null; then
  echo "Gunicorn is running. Proceeding to restart."
else
  echo "Gunicorn is not running. Starting gunicorn."
fi

# Send HUP signal to gracefully restart gunicorn
echo "Sending HUP signal to restart gunicorn..."
pkill -HUP gunicorn

# Wait a few seconds to ensure the process has been restarted
sleep 20

# Check if gunicorn restarted successfully
if pgrep gunicorn > /dev/null; then
  echo "Flask app has been restarted successfully!"
else
  echo "Failed to restart Flask app. Gunicorn process is not running."
fi
