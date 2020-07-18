#!/bin/bash

ACCESS_LOG='/var/log/squid/access.log'
WHITELIST='/etc/squid/whitelist'

grep '[http|CONNECT]' $ACCESS_LOG | awk '{print $7}' | sed -e 's/^http.*\/\/\([^\/]*\).*$/\1/' -e 's/^\([^:]*\).*$/\1/' | sort -k 2 -t '.' | uniq > $WHITELIST
