#!/usr/bin/env bash
set -e

cslc layout.csl -arch=wse3 --fabric-dims=20,20 --params=M:2,N:2 --fabric-offsets=4,1 -o out --max-inlined-iterations=1000000 --memcpy --channels 1
cs_python run2.py --name out