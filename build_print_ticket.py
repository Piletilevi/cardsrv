# coding: utf-8

from distutils.core import setup
import py2exe

OPTIONS = [
    {
        "script": "print_ticket.py",
        "dest_base": "print_ticket"
    }]

setup(
    options = {'py2exe': {'bundle_files': 1}},
    zipfile = None,
    console = OPTIONS
)

# run
# build_print_ticket.py py2exe
