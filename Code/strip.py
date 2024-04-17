import re

input_file = 'output.txt'
output_file = 'output2.txt'

def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()
    
    # Remove unwanted strings
    content = content.replace("!Toph|", "") 
    content = content.replace("|-", "")
    content = re.sub(r'\[.*?\] ', '', content)
    content = re.sub(r'\[.*?\]', '', content)

    # Remove unwanted punctuation and convert to lowercase
    content = content.replace("...", "")
    content = content.replace(". ", '\n')
    content = content.replace("! ", '\n')
    content = content.replace("? ", '\n')
    content = content.replace(".", "")
    content = content.replace(",", "")
    content = content.replace("'", "")
    content = content.replace('"', "")
    content = content.replace("?", "")
    content = content.replace("!", "")
    content = content.lower()
    
    # Remove empty lines
    lines = content.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    content = '\n'.join(non_empty_lines)

    with open(output_file, 'w') as f:
        f.write(content)

process_file(input_file, output_file)
