import argparse
from src.calc import Calculator


def main() -> None:
    parser = argparse.ArgumentParser(description='Calculator CLI')
    parser.add_argument('operation', choices=[
                        'add', 'subtract', 'multiply', 'divide'], help='Operation to perform')
    parser.add_argument('a', type=float, help='First number')
    parser.add_argument('b', type=float, help='Second number')

    args = parser.parse_args()

    # Check if all required arguments are provided
    if not args.operation or args.a is None or args.b is None:
        parser.print_help()
        return

    calc = Calculator()

    if args.operation == 'add':
        result = calc.add(args.a, args.b)
    elif args.operation == 'subtract':
        result = calc.subtract(args.a, args.b)
    elif args.operation == 'multiply':
        result = calc.multiply(args.a, args.b)
    elif args.operation == 'divide':
        result = calc.divide(args.a, args.b)

    print(
        f'The result of {args.operation} between {args.a} and {args.b} is: {result}')


if __name__ == '__main__':
    main()
