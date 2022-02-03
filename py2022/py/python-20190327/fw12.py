from fuzzywuzzy import process


strings = ['привет', 'здравствуйте', 'приветствую', 'хай', 'здорова', 'ку-ку']
res1=process.extract("Прив", strings, limit=4)
print(res1)
# [('привет', 90), ('приветствую', 90), ('здравствуйте', 45)]
res2=process.extractOne("Прив", strings)
# ('привет', 90)

print(res2[0])