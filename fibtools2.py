
def uptrend():
    print('\n\t\tUPTREND\t\n')
    print('Retracements\t\tExtensions\n')
    for r,e in zip(retracements,extensions):
        print(r,' = ',round((high - (diff * r/100)),2),'\t', e, ' = ', round((low + (diff * e/100)),2),'\n')

def downtrend():
    print('\n\t\tDOWNTREND\t\n')
    print('Retracements\t\tExtensions\n')
    for r,e in zip(retracements,extensions):
        print(r,' = ',round((low + (diff * r/100)),2),'\t',e, ' = ',round((high - (diff * e/100)),2),'\n')
    


trend = input("What is the trend? up or down: ")
high = float(input('Enter High: '))
low = float(input('enter Low: '))
diff = high - low
print('The difference between High and Low is :',diff)

retracements = [23.6,38.2,50.00,61.8,76.4,78.6,85.40]
extensions = [127.2,138.2,150.00,161.8,176.4,261.8,423.6]

if high > low:
    if trend == 'up':
        uptrend()

    elif trend == 'down':
        downtrend()

    else:
        print("Enter 'up' or 'down'")
else:
    print('High must always be greater than Low!!!!!')

    
