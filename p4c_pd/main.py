#!/usr/bin/env python3

# Copyright 2013-present Barefoot Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# Antonin Bas (antonin@barefootnetworks.com)
#
#

# -*- coding: utf-8 -*-

import argparse
import os
import sys
import json

from p4c_pd import (
    version,
    gen_pd
)

def get_parser():
    parser = argparse.ArgumentParser(description='p4c-pd arguments')
    parser.add_argument('--json', dest='json', type=str,
                        help='Generate PD from a JSON file',
                        required=True)
    parser.add_argument('--pd', dest='pd', type=str,
                        help='Generate PD C/C++ code for this P4 program'
                        ' in this directory. Directory must exist.',
                        required=True)
    parser.add_argument('--p4-prefix', dest='p4_prefix', type=str,
                        help='P4 name use for API function prefix',
                        default="prog", required=False)
    parser.add_argument('--version', action='version',
                        version=version.VERSION_NUMBER)
    return parser


# to be used for a destination file
def validate_path(path):
    path = os.path.abspath(path)
    if not os.path.isdir(os.path.dirname(path)):
        print(path, "is not a valid path because",\
            os.path.dirname(path), "is not a valid directory")
        sys.exit(1)
    if os.path.exists(path) and not os.path.isfile(path):
        print(path, "exists and is not a file")
        sys.exit(1)
    return path


# to be used for a source file
def validate_file(path):
    path = validate_path(path)
    if not os.path.exists(path):
        print(path, "does not exist")
        sys.exit(1)
    return path


def validate_dir(path):
    path = os.path.abspath(path)
    if not os.path.isdir(path):
        print(path, "is not a valid directory")
        sys.exit(1)
    return path


def main():
    parser = get_parser()
    (args, unparsed_args) = parser.parse_known_args()

    path_json = validate_file(args.json)
    path_pd = validate_dir(args.pd)
    with open(path_json, "r") as read_file:
        json_dict = json.load(read_file)

    gen_pd.generate_pd_source(json_dict, path_pd, args.p4_prefix)


if __name__ == "__main__":
    main()
