'''
Parse command line arguments
'''
import argparse  # ref. https://docs.python.org/2/howto/argparse.html


def get_arg(argName, allArgs=[], default=None):
  if not argName:
    return None

  value=default

  parser=argparse.ArgumentParser()

  for arg in allArgs:
    parser.add_argument(arg)

  args=parser.parse_args()
  if hasattr(args, argName):
    value=getattr(args, argName)

  return value

