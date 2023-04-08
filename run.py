#!/usr/bin/env python3

import sys
import os

THIS_DIR = os.path.dirname(__file__)

sys.path.insert(0, THIS_DIR)

import p4c_pd.main

if __name__ == "__main__":
    p4c_pd.main.main()
