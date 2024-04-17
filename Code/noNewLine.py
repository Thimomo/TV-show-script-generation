import os

input_dir = r'C:\Users\koenv\OneDrive - UvA\2023-2024\PAV\TTTV PAV\TTTV\Teksten'

def remove_newlines_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('\n', '')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_dir, filename)
        remove_newlines_from_file(file_path)
