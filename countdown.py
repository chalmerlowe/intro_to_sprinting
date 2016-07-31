#!/usr/bin/env python
####################################################################################################
#
# Template based on recommendations from Matt Harrison in Beginning Python Programming
#
'''Creating example function to contribute to GitHub repo
'''

# Imports
# Need sys because using it to call main with arguments
import argparse
import sys
import time

# Globals
# Note:  Consider using function/class/method default parameters instead of global constants where
# it makes sense
#BASE_FILE = 'file1'

# Metadata
__author__ = 'James R. Small'
__contact__ = 'james<dot>r<dot>small<at>outlook<dot>com'
__date__ = 'July 30, 2016'
__version__ = '0.0.1'


####################################################################################################
def countdown(start):
    '''Countdown from start.'''
    while start > 0:
        print('{} '.format(start), end='\r')
        start -= 1
        time.sleep(0.250)
    start = 79
    while start > 0:
        print('-', end='', flush=True)
        start -= 1
        time.sleep(0.005)
    print('')

####################################################################################################
def main(args):
    '''Process arguments and call countdown'''
    parser = argparse.ArgumentParser(description='Simple example program using a function')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-s', '--start', help='number to start countdown from', default=10,
                        type=int, metavar='STARTING_NUMBER')
    parser.add_argument('-v', '--verbose', action='store_true', help='display verbose output',
                        default=False)
    args = parser.parse_args()

    if args.verbose:
        print('Start = {}, type = {}'.format(args.start, type(args.start)))
    countdown(args.start)

# Call main and put all logic there per best practices.
# No triple quotes here because not a function!
if __name__ == '__main__':
    # Recommended by Matt Harrison in Beginning Python Programming
    # sys.exit(main(sys.argv[1:]) or 0)
    # Simplied version recommended by Kirk Byers
    main(sys.argv[1:])


####################################################################################################
# Post coding
#
# pylint <script>.py
#   Score should be >= 8.0
#
# Future:
# * Testing - doctest/unittest/other
# * Logging
#

