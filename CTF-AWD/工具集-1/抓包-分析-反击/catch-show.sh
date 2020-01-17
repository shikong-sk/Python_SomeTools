#!/usr/bin/env bash
if [ -f "catch.tmp" ]; then
    tail -f catch.tmp | sed 's/HTTP\/1.1.*,HTTP request [0-9]*\/[0-9]*,\?/     /g';
else
    echo '请先运行catch-real.sh抓包'
fi