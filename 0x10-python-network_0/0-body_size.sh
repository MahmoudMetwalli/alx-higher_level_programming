#!/usr/bin/env bash
curl -I "$1"|grep Content-Length| awk '{print $2}'
