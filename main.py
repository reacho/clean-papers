"""
*****************
** Walkthrough **
*****************

Which commands do you want to deal with?

> STKOUT:   remove the command,
            remove everything inside the curly brackets;
> REVIEW:   remove the command,
            keep everything inside the curly brackets;
> COMMENTS: remove everything on the right of "%" character.

True  --> I want to do what is written above.
False --> I want to leave the text as is.



******************
** Known issues **
******************

"DELETE_STKOUT" and "DELETE_REVIEW" do not work if the left and right curly brackets are not in the same line.

"""

DELETE_STKOUT   = True # Boolean: False or True 
DELETE_REVIEW   = True # Boolean: False or True 
DELETE_COMMENTS = True # Boolean: False or True 

input_file = "input.txt"  # Replace with your input file path
output_file = "output_test.txt"  # Replace with your output file path


#####################################################################
#####################################################################

import regex

def process_text_file(input_file, output_file):
    pat_stkout = regex.compile(r'\\stkout(\{(?:[^{}]++|(?1))++\})')
    pat_review = regex.compile(r'\\review(\{(?:[^{}]++|(?1))++\})')
    v_punctuation = [' ', '.', ',', ';', ':']

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for cont_line, line in enumerate(infile):
            
            if DELETE_STKOUT:
                REMOVED_STKOUT=False
                while pat_stkout.search(line) is not None:
                    REMOVED_STKOUT = True
                    line = line.replace(pat_stkout.search(line)[0], '')
                
                if REMOVED_STKOUT: 
                    if len(line)==0:
                        line = '%\n'
                    elif line.isspace():
                        line = '%\n'


            if DELETE_REVIEW:
                while pat_review.search(line) is not None:
                    line = line.replace(pat_review.search(line)[0], pat_review.search(line)[0][8:-1])


            if DELETE_COMMENTS:
                DELETE_THE_FOLLOWING = True
                LEN = len(line)
                for cont, letter in enumerate(line):
                    if letter == '%' and DELETE_THE_FOLLOWING and cont<LEN-1:
                        line = line[:cont+1] # regex.sub(line[cont+1:], '', line)
                        line = line + '\n'
                        break

                    if letter == "\\":
                        DELETE_THE_FOLLOWING = False
                    else:
                        DELETE_THE_FOLLOWING = True
            
            for punctuation in v_punctuation:
                line = line.replace(f' {punctuation}', f'{punctuation}')

            
            # Write the modified line to the output file
            outfile.write(line)


line = process_text_file(input_file, output_file)
print(f"Processing complete. Output saved to {output_file}")
