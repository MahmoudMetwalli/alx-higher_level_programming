#!/bin/bash
# sends JSON POST as the first arg,& displays body
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
