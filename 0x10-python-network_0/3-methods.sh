#!/bin/bash
# Prints avaiable options
curl -i -X OPTIONS "$1"| grep Allow|sed 's/Allow: //'
