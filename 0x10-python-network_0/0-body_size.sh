#!/bin/bash
# Displays the size of the body of the response
curl -I "$1"|grep Content-Length| awk '{print $2}'
