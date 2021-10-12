"""CLI Calculator using ArgumentParser."""

from argparse import ArgumentParser

from calc import sum_, sub, mult, div


parser = ArgumentParser(description='Calculator')

parser.add_argument('--sum', help='Sum operation', action='store_true')
parser.add_argument('--sub', help='Subtraction operation', action='store_true')
parser.add_argument('--mult', help='Multiplication operation', action='store_true')
parser.add_argument('--div', help='Division operation', action='store_true')
parser.add_argument('x', type=int, help='First value')
parser.add_argument('y', type=int, help='Second value')

args = parser.parse_args()

if args.sum:
    print(f'{sum_(args.x, args.y)}')

if args.sub:
    print(f'{sub(args.x, args.y)}')

if args.mult:
    print(f'{mult(args.x, args.y)}')

if args.div:
    print(f'{div(args.x, args.y)}')
