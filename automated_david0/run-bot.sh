#!/usr/bin/env bash

while true; do
  sleeptime=$(( ( RANDOM % 21600 ) + 3600 ))
  python3 automated_david0.py
  echo "Tweet Sent. Waiting $sleeptime seconds" >> nohup.out
  sleep $sleeptime
done