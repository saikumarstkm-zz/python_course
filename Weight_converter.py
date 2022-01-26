weight = float(input('Weight: '))
char = input('(L)bs or (K)g: ')
if char.upper() == 'L':
    conv_weight = 0.45 * weight
    print(f'You are {conv_weight} kilograms')
elif char.upper() == 'K':
    conv_weight = 2.2 * weight
    print(f'You are {conv_weight} kilograms')