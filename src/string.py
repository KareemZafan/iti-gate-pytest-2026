
def reverse_string(s):
    return s[::-1]

## level, madam, racecar, iti 
def is_plindrome(s):
    cleaned = ''.join(s.split()).lower()
    return cleaned == cleaned[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count    

def is_uppercase(s):
    return s.isupper()

def is_lowercase(s):
    return s.islower()
