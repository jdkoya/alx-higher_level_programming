#!/usr/bin/python3 
"""Defines MyList class that inherits form list."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in ascending order."""
        print(sorted(self))
