from tkinter import E


height = float(input('Put your height : '))
sex = int(input('You are boy[1] or girl[2]: '))
if sex == 1:
    print(f'Your ideal weight is : {(height*72.7)-58}')
elif sex == 2:
    print(f'Your ideal weight is : {(height*62.1)-44.7}')
