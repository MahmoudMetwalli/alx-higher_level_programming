#!/bin/bash
# Display post params
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -d  "$1"
