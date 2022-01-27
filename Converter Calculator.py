#   Write a program that converts days in seconds, Celsius in Fahrenheit, miles in centimeters.
days = int(input('Enter number of days to convert : '))
print(f'days in seconds : {days*24*60*60}')

temp_c = float(input('Enter temperature in celsius : '))
print(f'Temperature in Fahrenheit : {temp_c*1.8+32}')

miles = float(input('Enter value in miles : '))
print(f'Distance in centimeters : {miles*160934.4}')
