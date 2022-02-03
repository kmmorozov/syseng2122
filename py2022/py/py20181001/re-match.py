import re

s = '7Kirill777@mail.rujkadfshajkshfjkasdhfjk alex@gmail.com '

#pattern = re.compile(r'[a-z0-9]+@[a-z]+\.[a-z]+',re.I)
pattern = re.compile(r'\w+@\w+\.\w{0,7}\ ',re.I)
#pattern = re.compile(r'[^,]+',re.I)
math = pattern.findall(s)
print(math)



#[0-9] \d
#[^0-9] \D
#[0-9a-z] \w
#[^0-9a-z] \W
#
#