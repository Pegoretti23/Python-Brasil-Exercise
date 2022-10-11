archive = float(input('file size in MB : '))
vel = float(input('Speed of internet in Mbps : '))
time = (archive/(vel/8))/60
print(f'it will take approximately {time:.0f} minutes')