import argparse
import glob
import os


# Functions supported by the demo
# TODO: add more functions

def demo_sum(numbers):
    return sum(numbers)

def demo_avg(numbers):
    return sum(numbers) / len(numbers)

def demo_max(numbers):
    return reduce(max, numbers)

def demo_min(numbers):
    return reduce(min, numbers)


if __name__ == '__main__':

    # Parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', action='store', help="A file to process (all under data/ by default)", default=None)
    args = parser.parse_args()

    # Choose which function we'll apply
    # TODO: choose with command-line options
    func = demo_max

    # Process all files under data/ if no file is given
    fnames = [args.file] if args.file else glob.glob('data/*')

    for fname in fnames:
        print("Processing %s" % fname)

        with open(fname, 'rt') as f:
           numbers = [float(x) for x in f]
           print('%s: %r' % (func.__name__, func(numbers)))
