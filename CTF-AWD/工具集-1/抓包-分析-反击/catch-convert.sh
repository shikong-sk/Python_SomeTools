#!/usr/bin/env bash
if [ -f "catch.tmp" ]; then
    cp -f catch.tmp catch.log ;sed -i 's/HTTP\/1.1.*,HTTP request [0-9]*\/[0-9]*,\?/     /g' catch.log
fi