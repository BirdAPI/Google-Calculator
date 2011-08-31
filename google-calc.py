#!/usr/bin/python

from Google import google
from Google.google import Google

__author__ = "Anthony Casagrande <birdapi@gmail.com>"
__version__ = "0.3"

def main():
    prev = None
    print "Enter an expression, or 'q' to exit.\n"
    while True:
        input = raw_input()
        if input == "quit" or input == "q" or input == "exit":
            break
        result = Google.calculate(input)
        if result:
            print "=", result.value, result.unit if result.unit else ""
        else:
            print "No Result!"
        prev = result

if __name__ == "__main__":
    main()
