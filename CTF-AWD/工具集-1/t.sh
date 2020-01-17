#!/usr/bin/env bash
echo `dirname $0`
echo `dirname /s`
shellPath=$(cd "$(dirname "$0")"; pwd)
echo $shellPath