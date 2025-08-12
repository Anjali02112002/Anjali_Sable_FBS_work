sub1 = int(input('Enter marks of first subject : '))
sub2 = int(input('Enter marks of second subject :'))
sub3 = int(input('Enter marks of third subject :'))
sub4 = int(input('Enter marks of fourth subject :'))
sub5 = int(input('Enter marks of fifth subject :'))

sum = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (sum/500)*100

if (percentage > 90):
    print('The student has passed in distiction ')
elif (percentage > 80 and percentage < 90):
    print('The student has passed in firts class')
elif (percentage > 65 and percentage < 80):
    print('The student has passed in second class')
elif(percentage > 35):
    print('The student has passed the exam')
else:
    print('The student is fail')
