'''
Parse command line arguments
'''
import argparse  # ref. https://docs.python.org/2/howto/argparse.html


def get_arg(argName, default=None):
  value = default

  parser=argparse.ArgumentParser()
  parser.add_argument(argName)
  args=parser.parse_args()
  if hasattr(args, argName):
    value=getattr(args, argName)

  return value

