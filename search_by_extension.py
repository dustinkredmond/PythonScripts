#!/usr/bin/env python3

import os

search_dir = input('Enter a search directory: ')
ext = input('Enter a file extension: ')
for f in os.listdir(search_dir):
    if f.endswith(ext) or f.endswith('.'+ext):
        print(f)

