#! /usr/bin/env python3

"A module for getting each matched word and line it was found on from a specified regular expression string."

import sys
import re

def get_re_output(n, input, output):
    """ 
    Outputs a list of words matching a search string and line numbers found on. 
    
    Parameters
    ----------
    n : str
        The string to be searched for in the desired input file.
    input: file
        The file to be searched for the desired string.
    output: file
        The file for output to be written to. 

    Returns
    ------
    None

    Examples
    -------
    >>> get_re_output("is", "test.txt", "testoutput2.txt")
    Opening input file
    Done!
    input file is closed? True
    output file is closed? True

    """
    REpattern_obj = re.compile(n, re.IGNORECASE)


    with open(input, 'r') as in_stream:
        print('Opening input file')
        with open(output, 'w') as out_stream:
            for line_index, line in enumerate(in_stream, 1):
                if REpattern_obj.findall(line):
                    match = REpattern_obj.search(line)
                    out_stream.write("{0}\t{1}\n".format(line_index, match.group()))
    print('Done!')
    print('input file is closed?', in_stream.closed)
    print('output file is closed?', out_stream.closed)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(sys.argv[0] + ": Expecting three command line arguments -- the search string, the input file name to search, and the desired output file name")
    n = sys.argv[1]
    input = sys.argv[2]
    output = sys.argv[3] 
    re_output = get_re_output(n, input, output) 


