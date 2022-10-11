def canofink(area):
    areaink = area/3
    can = 1
    while areaink >18:
        can += 1
        areaink -= 18
    return can
def gallonofink(area):
    areaink = area/3
    gallon = 1
    while areaink > 3.6:
        gallon += 1
        areaink -= 3.6
    return gallon
def gallonandcan(area):
    areaink = (area/3)+(area*0.1)
    can = 0
    gallon = 0
    while areaink > 18:
        can += 1
        areaink -=18
    while areaink > 3.6:
        gallon += 1
        areaink -= 3.6
    return can, gallon        

area = float(input('What is the area in mt2 to be painted: '))
can = canofink(area)
gallon = gallonofink(area)
all = gallonandcan(area)
print(f'buying only 18 lt cans you will need {can} and spend R${can*80}')
print(f'buying only 3.6 lt gallon you will need {gallon} and spend R${gallon*25}')
print(f'buying cans and gallons you need cans {all[0]}, Gallons {all[1]} and spend {(all[0]*80)+(all[1]*25)}')