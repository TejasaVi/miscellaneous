#!/usr/bin/python

import argparse

'''
#TODO:
1. Remove the commented lines and then parse
2. Condition of a single-line code
'''

def if_else_checker(input_data):
    cntr = 0
    tracker_list = []
    if_cntr = else_cntr = 0
    for line in input_data:
        cntr += 1
        if line.lstrip().startswith('#') or line.lstrip().startswith('//'):
            continue
        if ("elif" in line) or ("else if" in line):
            continue
        if "if" in line:
            if_cntr += 1
            tracker_list.append(("if",cntr))
        elif "else" in line and (if_cntr > 0):
            if_cntr -= 1
            tracker_list.append(("else",cntr))
        elif "else" in line and (if_cntr <= 0):
            else_cntr += 1
            tracker_list.append(("else",cntr))

    if (if_cntr == else_cntr) and  (if_cntr == 0):
        print "TEST PASSED"
    elif if_cntr < 0 or else_cntr < 0:
        print "Syntax error with missing if/else block"
    elif if_cntr > 0:
        print "if statements without else block present"
        print tracker_list
    elif else_cntr > 0:
        print "else block without if are present"
        print tracker_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My Script")
    parser.add_argument("-i", "--input_file",required=True)
    results = parser.parse_args()
    with open(results.input_file) as file:
        #data = [line for line in file.readlines() if not line.lstrip().startswith('#') and not line.lstrip().startswith('//')]
        data = file.readlines()

    if_else_checker(data)
