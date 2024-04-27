#!/bin/bash
# Prints avaiable options
curl -si -X OPTIONS "$1"| grep Allow|sed 's/Allow: //'
