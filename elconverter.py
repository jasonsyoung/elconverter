#!/usr/bin/env python3

"""
elconverter

This application parses Element Lists found in a
directory and converts them to SRT caption format

"""

import os
from optparse import OptionParser
from runner import Runner

def main():
    parser = OptionParser()
    parser.add_option("-d", "--directory", dest="directory",
                      help="directory to process (defaults to current directory)", metavar="FILE")
    parser.add_option("-s", "--include-speaker", action="store_true", dest="include_speaker")
    parser.add_option("-t", "--exclude-tags", action="store_false", dest="include_soundtags")

    (options, args) = parser.parse_args()

    if options.directory is None:
        directory = os.getcwd()
    else:
        directory = os.path.realpath(options.directory)
        if not os.path.isdir(directory):
            raise "Directory not found"

    Runner(directory, options.include_speaker, options.include_soundtags)


if __name__ == "__main__":
    main()