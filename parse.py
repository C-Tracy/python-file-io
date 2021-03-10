import re

REpattern_string = "\w*herit\w*"
REpattern_obj = re.compile(REpattern_string, re.IGNORECASE)


with open('origin.txt', 'r') as in_stream:
    print('Opening origin.txt')
    #content = in_stream.read()
    #print(REpattern_obj.findall(content))
    with open('output_inheritance.txt', 'w') as out_stream:
        for line_index, line in enumerate(in_stream, 1):
            #print(REpattern_obj.findall(line))
            #line = line.strip()
            #match = re.findall('\w*herit\w*', line)
            if REpattern_obj.findall(line):
                match = REpattern_obj.search(line)
                out_stream.write("{0}\t{1}\n".format(line_index, match.group()))
        #print(match)
            #out_stream.write('line_index\tmatch\n'.format(word, word))
print('Done!')
print('dummy.txt is closed?', in_stream.closed)
print('output.txt is closed?', out_stream.closed)
