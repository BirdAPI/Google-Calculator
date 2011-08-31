#!/usr/bin/python

from Google import google
from Google.google import Google

def main():
    prev = None
    print "Enter an expression, or 'quit' to exit.\n"
    while True:
        string = raw_input()
        if string == "quit":
            break
        result = Google.calculate(string)
        if result:
            print "=", result.value, result.unit if result.unit else ""
        else:
            print "No Result!"
        prev = result

if __name__ == "__main__":
    main()
