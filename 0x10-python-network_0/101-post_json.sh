#!/bin/bash
# sends JSON POST as the first arg,& displays body
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"
