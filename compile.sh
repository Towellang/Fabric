#!/bin/bash

nuitka --recurse-all --standalone towel.py

rm -rf towel.build
mv towel.dist build
mv build/towel.exe build/towel
