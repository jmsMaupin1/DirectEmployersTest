import argparse
import sys

def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string", help="The string you would like reversed")
    
    args = parser.parse_args(args=None if sys.argv[1:] else ['-h'])

    print(reverse_string(args.string))
    
