#payroll hours and rate include overtime

def payroll(hours, rate):
#compare if hours is overtime or regular
	if hours <= 40:
		pay=hours*rate
	else:
		overhours = hours-40
		overtime = (overhours*1.5)*rate
		pay = (40*rate) +  overtime

	
	print "Total Pay", pay
	netpay=pay*0.8874
	print ('Net Pay:''%.2f'%netpay)
	return 0

while True:

	hours = input('Enter hours: or 0 for Calendar ')
	if hours !=0:
		rate = input('Enter rate: ')
	
		print payroll(hours, rate)
	else:
		
		break	
#calendar selected enter date
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
#Today's date
d1 = datetime.datetime.today()
d2 = ObtainDate()
d3 = d2 - d1 
print d3

#calculate vacation days
v = (d3.days * (20.0/365))
print int(v)


#print calendar
#print ObtainDate()
#print 
#import calendar
#cal = (calendar.month(2019,03))
#print cal


