#!/bin/zsh

grep -i "GET" access.log
grep "10.0.0.5" access.log
grep -C 1 "10.0.0.5" access.log
grep -c "GET" access.log
grep -c "POST" access.log
grep "404" access.log 
grep "403" access.log 
grep -E"404|03" access.log 
grep -E "404|403" access.log 
grep -E --color=always "403|404" access.log
grep -E "403|404" access.log | awk '{print $1}'
grep -E "403|404" access.log | awk '{print $1}' | sort -u
grep -E "403|404" access.log | awk '{print $1}' | sort | uniq -c | sort -nr
grep -E "403|404" access.log | awk '{print $1}'
awk '{print $1, $7}' access.log
grep "404" access.log | awk '{print $1, $7}'
Example: Find all 403 errors, but ignore the ones from your own IP (e.g., 1.2.3.4), and show the URL:\n\nBash\ngrep "403" access.log | grep -v "1.2.3.4" | awk '{print $7}'
grep "403" access.log | grep -v "1.2.3.4" | awk '{print $7}'
grep -E "403|404" access.log | grep -v "1.2.3.4" | awk '{print $7}'
