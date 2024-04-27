#!/bin/bash
# sends JSON POST as the first arg,& displays body
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
