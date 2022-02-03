shoplist = ['морковь','яблоки','апельсины','бананы','клубника']
print(f'В моей корзине будет {len(shoplist)} покупок')
print('Звонит жена')
shoplist.append('киви')
print(f'Теперь в моей корзине будетет {len(shoplist)} покупок')
#for pokupka in shoplist:
#    print(f'сегодня я куплю: {pokupka}')
shoplist.sort()

print(f'После сортировки')
for pokupka in shoplist:
    print(f'сегодня я куплю: {pokupka}')

print(f'Первое что нужно купить - {shoplist[0]}')

for i in range(1,len(shoplist)+1):
    vrukah = shoplist[0]
    del shoplist[0]
    print(f'положил в корзину {vrukah}')
    print('осталось купить', shoplist)
    
    
    
    
    
    
    
    
    
