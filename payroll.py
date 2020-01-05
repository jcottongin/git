#payroll hours and rate include overtime

def payroll(hours, rate):
#compare if hours is overtime or regular
	if hours <= 40:
		pay=hours*rate
	else:
		overhours = hours-40
		overtime = (overhours*1.5)*rate
		pay = (40*rate) +  overtime

	print 'Federal:','%.2f'%(pay*0.07)
	print 'Medicare:','%.2f'%(pay*0.05)
	print 'Social Security:','%.2f'%(pay*.01)
	print "Total Pay: ", pay
	netpay=pay*0.7374
	print 'Weekly Net Pay:''%.2f'%netpay
	print 'Monthly Net Pay: ', netpay*4
	print 'Net Yearly:' , netpay*52

##adding set hours and rate
#while True:
#	entry = input('1 for hours 0 for calendar')	
#	if entry !=0:
#		print('Enter hours''\n''or 0 for Calendar ''\n')
#		hours = 40
#		print 'hours: ', hours
#		rate = 30
#		print'rate: ', rate
#	
#		print payroll(hours, rate)
#	else:
#		break
##
#user input for hour and pay variables 
while True:

	hours = input('Enter hours: or 0 for Calendar ')
	if hours !=0:
		rate = input('Enter rate: ')
	
		print payroll(hours, rate)
	else:
		
		break	
##
#calendar selected enter date
import datetime
def ObtainDate():
    isValid=False
    while not isValid:
        userIn = raw_input("Enter Date ")
        try: # strptime throws an exception if the input doesn't match the pattern
            d = datetime.datetime.strptime(userIn, "%m/%d/%y")
            isValid=True
        except:
            print "Enter Date in mm/dd/yy format"

    return d

d1 = datetime.datetime.today() #Today's date
d2 = ObtainDate()  #Return value of user entered date
d3 = d2 - d1 #Difference in days entered and today
print d3

#calculate vacation days
print  "Today is ", d1.strftime("%m/%d/%Y")
v = (d3.days * (20.0/365))
print  "Vacation Days", int(v) 


#print calendar
#print ObtainDate()
#print 
#import calendar
#cal = (calendar.month(2019,03))
#print cal
