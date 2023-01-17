!#/bin/bash
# send a request to a URL and display the content size in bytes
curl -s "$1" | wc -c
