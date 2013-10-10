#! /usr/bin/python
#WIP argument parser for 


import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
#parser.add_argument("echo", help="echo the string you use here")
group = parser.add_mutually_exclusive_group()


group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true",
                    help="Simple interface")

parser.add_argument("x", 
                     help="The Base",
                     type=int)
parser.add_argument("y", 
                     help="The Exponent",
                     type=int)
args = parser.parse_args()

answer = args.x **args.y

#print args.square**2
if args.quiet:
    print answer
elif args.verbose:
    print "{0} to the power of {1} equals {2}".format(args.x, args.y, answer)
else:
    print "{0}^{1} == {2}".format(args.x, args.y, answer)

