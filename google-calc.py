#!/usr/bin/python

from Google import google
from Google.google import Google

__author__ = "Anthony Casagrande <birdapi@gmail.com>"
__version__ = "0.3"

def main():
    prev = None
    print "Enter an expression, or 'q' to exit.\n"
    while True:
        string = raw_input()
        if string == "quit" or string == "q" or string == "exit":
            break
        result = Google.calculate(string)
        if result:
            print "=", result.value, result.unit if result.unit else ""
        else:
            print "No Result!"
        prev = result

if __name__ == "__main__":
    main()
