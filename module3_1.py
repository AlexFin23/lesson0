calls = 0

def string_info(string):
    global calls
    calls += 1
    string = len(string), string.upper(), string.lower()
    return string

def is_contains(string,list_to_search):
    global calls
    calls += 1
    string = string.upper()
    line1 = ''.join(list_to_search)
    line1 = line1.upper()
    if string in line1:
        return True
    else:
        return False












print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)