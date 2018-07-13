"""
Encodes and runs a ROS Code file
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
# Main Modules
from builtins import open
from builtins import str
from sys import argv as args
from sys import exit as exitexc
import syntax
# Initialise Backwards Compatibility
from future import standard_library
standard_library.install_aliases()

try:
    args[1]
except IndexError:
    print("ERROR: No ROS Code file provided in execution arguments")
    print("Ensure the execution code looks something like this: python run-file.py test.ros")

with open(args[1]) as f:
    IGNORELINE = False
    CONTENT = f.readlines()
    CONTENT = [x.strip() for x in CONTENT if x.strip()]
    for value in enumerate(CONTENT):
        if not(value[1].startswith('!')) and IGNORELINE is False:
            firstpart = value[1].split(".")[0]
            lenoffirstpart = len(value[1].split(".")[0])
            afterpart = str(value[1][lenoffirstpart + 1:])
            apwithcomma = afterpart.replace(".", "', '")
            preprint = str(firstpart + "(" + apwithcomma + ")")
            printtext = preprint.replace("(", "('")
            lastprinttext = printtext.replace(")", "')")
            try:
                exec(str("syntax." + lastprinttext))
            except Exception as exc:
                template = "ERROR: An error of type {0} occured while running line {1} because {2}"
                message = template.format(
                    type(exc).__name__, str(value[0] + 1), str(exc.args[0]))
                print(message)
                exitexc(1)
        elif value[1].startswith('!!!'):
            IGNORELINE = not IGNORELINE

exitexc(0)
