#!/usr/bin/env python

# This is a simple Python program.
# Ask for a name and say hello to it.

while True:
    userName = raw_input("What is your name: ")

    if userName:
        print("Hello " + userName)
    else:
        print("Goodbye")
        break


