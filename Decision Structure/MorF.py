sex = str(input("You're Female[F] or Male[M] : ")).lower()

print(f'{sex}')
if sex == 'f':
    print("You're a Female")
elif sex == 'm':
    print("You're a Male")
else:
    print('Invalid sex')