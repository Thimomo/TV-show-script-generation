import os
import re

# Mijn Git Directory
input_dir = r'C:\Users\koenv\OneDrive - UvA\2023-2024\PAV\TTTV PAV\TTTV\Teksten'
output_file = 'output.txt'

pattern = re.compile(r'!Toph\|.*?\|-', re.DOTALL)

with open(output_file, 'w', encoding='utf-8') as outfile:
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            filepath = os.path.join(input_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as infile:
                for line in infile:
                    matches = pattern.findall(line)
                    for match in matches:
                        outfile.write(match.strip() + '\n')
