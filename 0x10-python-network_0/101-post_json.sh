#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -sX POST -H "Content-type: application/json" -H "Accept: application/json" -d "@$2" "$1"
