#!/usr/bin/env python3

"""
elconverter

This application parses Element Lists found in a
directory and converts them to SRT caption format

"""

import os, sys
from optparse import OptionParser
from elconverter.runner import Runner

def main():
    usage = "usage: %prog [options] source_directory"
    parser = OptionParser(usage=usage)
    parser.add_option("-s", "--include-speaker", action="store_true", dest="include_speaker")
    parser.add_option("-t", "--exclude-tags", action="store_false", dest="include_soundtags")

    (options, args) = parser.parse_args()

    if len(args) > 1:
        print("Too many arguments, please specify one directory", file=sys.stderr)
        sys.exit(1)

    directory = os.path.realpath(args[0])
    if not os.path.isdir(directory):
        print("'{}' is not a valid directory".format(args[0]), file=sys.stderr)
        sys.exit(2)

    Runner(directory, options.include_speaker, options.include_soundtags)


if __name__ == "__main__":
    main()