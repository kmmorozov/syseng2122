import re

st = 'AV Analytics Vidhya AV analytics'

# result = re.match(r'Analytics', st)
# print(result)
# print(result.group(0))


# result = re.search(r'Analytics', st)
# print(result)
# print(result.group(0))

# result = re.findall(r'Analytics', st,re.I)
# print(result)

# result = re.split(r'y', st,re.I)
# print(result)

result = re.sub(r'Analytics', 'XZXZXZXZ', st)
print(result)
 







