import re
print(re.findall(r'\S', 'fycs sycs tycs 123456'))
print(re.findall(r'\d', 'fycs sycs tycs 123456'))
print(re.findall(r'\D', 'fycs sycs tycs 123456'))
print(re.split(r'\s', 'fycs sycs tycs 123456'))
print(re.findall(r'\s', 'fycs sycs tycs 123456'))
print(re.findall(r'\A', 'fycs sycs tycs 123456'))
print(re.findall(r'\z', 'fycs sycs tycs 123456'))
print(re.findall(r'\c|c', 'fycs sycs tycs 123456'))
