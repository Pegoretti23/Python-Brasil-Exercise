fish = float(input('what is the weight of the fish on KG? '))
if fish > 50:
    overweight = fish-50
    penalty = overweight*4
    print(f'Your fish is overweight in {overweight} kg ')
    print(f'Your penalty for this fish is R${penalty}')
else: 
    print(f'there will be no fine, weight within the limit')
    