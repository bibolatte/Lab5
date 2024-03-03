import re

def match_pattern(input_string):
    pattern = re.compile(r'^a(b*)$')

    if pattern.match(input_string):
        print(f'The string "{input_string}" matches the pattern.')
    else:
        print(f'The string "{input_string}" does not match the pattern.')


#2
def match_pattern(input_string):
    pattern = re.compile(r'ab{2,3}')
    match = pattern.fullmatch(input_string)

#3
def find_sequences(input_string):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    matches = pattern.findall(input_string)


#4
def find_sequences(input_string):
    pattern = re.compile(r'[A-Z][a-z]+')
    matches = pattern.findall(input_string)

#5
def match_pattern(input_string):
    pattern = re.compile(r'a.*b$')
    match = pattern.match(input_string)

#6
def replace_characters(input_string):
    pattern = re.compile(r'[ ,.]+')
    result = re.sub(pattern, ':', input_string)
    print(result)

#7
def snake_to_camel(snake_case_str):
    words = snake_case_str.split('_')
    camel_case_str = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case_str

#8
def split_at_uppercase(input_string):
    result = re.findall(r'[A-Z][^A-Z]*', input_string)
    return result

#9
def insert_spaces(input_string):
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return result

#10
def camel_to_snake(camel_case_str):
    result = ''.join(['_' + i.lower() if i.isupper() else i for i in camel_case_str]).lstrip('_')
    return result