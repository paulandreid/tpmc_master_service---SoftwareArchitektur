#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mtpproject.settings') #imports our settings for the project
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:  #check to see if Django is properlly installed
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH constants variable? Did you "
            "forget to activate a virtual constants?"
        ) from exc
    execute_from_command_line(sys.argv)  #executes the project


if __name__ == '__main__':
    main()
