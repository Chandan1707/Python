import re

string = 'hello i am chandan, roll 31 and tanusree roll 39, alins'
pattern = '[aeiou]'
# replace = '43'
result = re.findall(pattern, string)
length = len(result)
print(result)
print(length)
count = 0
for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
print(count)
