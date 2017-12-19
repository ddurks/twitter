#!/usr/bin/env bash

while true; do
  echo "Re-starting Django runserver"
  sleeptime=$(( ( RANDOM % 21600 ) + 3600 ))
  nohup python3 automated_david0.py
  sleep $sleeptime
done