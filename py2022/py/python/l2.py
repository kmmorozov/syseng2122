shoplistw = ['морковь','яблоки','апельсины','бананы','клубника','шаверма']
shoplistm = ['пиво','вобла','шашлык','шаверма','дошик']

shoplistw.extend(shoplistm)




print(f'Теперь в моей корзине будетет {len(shoplistw)} покупок')

shoplistw.sort()
print(f'После сортировки')
for pokupka in shoplistw:
    print(f'сегодня я куплю: {pokupka}')


print(shoplistw.count('шаверма'))

