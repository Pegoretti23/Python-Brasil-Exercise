salary = float(input('how much do you earn per hour ? '))
hour = float(input('how many hours do you work per month ? '))
grosssalary = salary*hour
intax =grosssalary*0.11
inss =grosssalary*0.08
sindicate =grosssalary*0.05
liqsal =grosssalary-intax-inss-sindicate 
print(f'You salary gross {grosssalary}')
print(f'Income Tax {intax}')
print(f'INSS Tax {inss}')
print(f'Sindicate Tax {sindicate}')
print(f'Net salary {liqsal}')