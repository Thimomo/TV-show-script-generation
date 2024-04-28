import re

input_file = 'output.txt'
output_file = 'output2.txt'

def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()
    
    # Remove unwanted strings
    content = re.sub(r'\[.*?\] ', '', content)
    content = re.sub(r'\[.*?\]', '', content)

    # Remove unwanted punctuation and convert to lowercase

    replacement = {
                    "!Toph|": "",
                    "|-": "",
                    "...": "",
                    # note the spaces
                    ". ": '\n',
                    "! ": '\n',
                    "? ": '\n',
                    ".": "",
                    ",": "",
                    "'": "",
                    '"': "",
                    "?": "",
                    "!": ""
                    }
    
    for case, sub in replacement.items():
        content.replace(case, sub)

    content.lower()

    # Remove empty lines
    lines = content.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    content = '\n'.join(non_empty_lines)

    with open(output_file, 'w') as f:
        f.write(content)

process_file(input_file, output_file)
