#!/usr/bin/env python2.7
import argparse
import os
import subprocess
import sys

"""
cd+ adds extra features to the command that you probably use more then anything
else

    Dot completion
        Say your in /foo/bar/foobar/baz/foobaz/bazfoo and you want to go to foobar.
        Traditionally, you would have to type ../../../ to get to foobar
        Now you can just do "cd+ foobar" instead
"""

def parse_options():
    p = argparse.ArgumentParser(description="cd+",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument("target")
    return p.parse_args(sys.argv[1:])


def run():
    args = parse_options()
    cwd = os.getcwd().split("/")[1:]  # first entry is ''
    try:
        found = cwd.index(args.target)
    except ValueError:
        return
    dots = len(cwd) - found - 1
    dots = "/".join([".." for i in xrange(dots)])
    subprocess.call(" cd %s && ls " % dots, shell = True)

if __name__ == '__main__':
    run()
