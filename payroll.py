#payroll hours and rate include overtime


def payroll(hours, rate):
	if hours <= 40:
		pay=hours*rate
		netpay = pay*.80

	else:
		overhours = hours-40
		overtime = (overhours*1.5)*rate
		pay = (40*rate) +  overtime
		netpay = pay*.80
	print 'pay:',pay 
	print 'netpay:', netpay
	return 

	
while True:

	hours = input('Enter hours: or 0 for Calendar ')
	if hours !=0:
		rate = input('Enter rate: ')
	
		print payroll(hours, rate)
	else:
		
		break	

import datetime
def ObtainDate():
    isValid=False
    while not isValid:
        userIn = raw_input("enter date ")
        try: # strptime throws an exception if the input doesn't match the pattern
            d = datetime.datetime.strptime(userIn, "%m/%d/%y")
            isValid=True
        except:
            print "Doh, try again!"

    return d


#test the function
print ObtainDate()
print 
import calendar
cal = calendar.month(2019, 1)
print cal

