import sys

 #print(sys.argv)


import argparse

#definition
parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True)
parser.add_argument("--age", type=int, default=30)
parser.add_argument('--music', choices=['rock', 'pop', 'classic'])

#analyse
args = parser.parse_args()

print(f"Bonjour {args.name}, vous avez {args.age} ans.")