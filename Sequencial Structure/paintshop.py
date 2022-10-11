area = float(input('What is the area in mt2 to be painted: '))
areaink = area/3
can = 1
while areaink > 18:
    can +=1
    areaink -= 18
print(f'You will have to buy {can} cans that cost R${can*80}')
