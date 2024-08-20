#!/bin/bash

# Function to send a message with retries
send_message() {
  local message=$1
  local retries=5
  local delay=1

  for ((i=1; i<=retries; i++)); do
    echo "$message" | nc -v -w 0 localhost 514
    if [ $? -eq 0 ]; then
      return 0
    fi
    sleep $delay
  done

  echo "Failed to send message after $retries attempts: $message" >&2
  return 1
}

# if $1 is set, send that many messages
if [ -n "$1" ]; then
  for i in $(seq 1 $1); do
    send_message "<14>$(hostname) message number $i"
  done
else
  send_message "<14>$(hostname) message number 1"
fi

# echo '<14>_sourcehost_ messagetext' | nc -v -w 0 localhost 514