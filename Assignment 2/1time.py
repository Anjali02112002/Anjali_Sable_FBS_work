#convert the time given in hour minute and seconds in seconds 

hour = int(input('Enter hour :'))
minute = int(input('Enter minute :'))
sec = int(input('Enter seconds :'))

sec1= hour*3600

sec2 = minute*60

total_sec = sec1 + sec2 + sec

print(f'Total seconds in {hour} hour {minute} minute and {sec} sec is {total_sec}')