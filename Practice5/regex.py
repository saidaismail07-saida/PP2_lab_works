#1
import re

s = input("Enter string: ")

if re.fullmatch(r'ab*', s):
    print("Match")
else:
    print("No match")


#2
import re

s = input("Enter string: ")

if re.fullmatch(r'ab{2,3}', s):
    print("Match")
else:
    print("No match")


#3
import re

s = input("Enter string: ")

matches = re.findall(r'[a-z]+(?:_[a-z]+)+', s)
print(matches)


#4
import re

s = input("Enter string: ")

matches = re.findall(r'[A-Z][a-z]+', s)
print(matches)


#5
import re

s = input("Enter string: ")

if re.fullmatch(r'a.*b', s):
    print("Match")
else:
    print("No match")


#6
import re

s = input("Enter string: ")

result = re.sub(r'[ ,.]', ':', s)
print(result)


#7
s = input("Enter snake_case string: ")

camel = ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(s.split('_')))
print(camel)


#8
import re

s = input("Enter CamelCase string: ")

parts = re.findall(r'[A-Z][a-z]*', s)
print(parts)


#9
import re

s = input("Enter string: ")

result = re.sub(r'([A-Z])', r' \1', s).strip()
print(result)


#10
import re

s = input("Enter CamelCase string: ")

snake = re.sub(r'([A-Z])', r'_\1', s).lower().lstrip('_')
print(snake)