#!/bin/bash
# a script that takes a url and sends a post to the passed url
curl -s -x POST -d "email=test@gmail.com.com&subject=I will always be here for you" "$1"
