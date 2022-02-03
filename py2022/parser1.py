base_link = 'https://www.avito.ru/sankt-peterburg/transport?cd=1&p=1&q=tohatsu+18'

bl_start = base_link[:54]
bl_end = base_link[55:]

print(bl_start)
print(bl_end)

for i in range(0,16):
    print(f'{bl_start}{i}{bl_end}')