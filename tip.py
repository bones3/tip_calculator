import sys

PURPOSE = '''\
Synopsis
Purpose - tip.py Amount people tip_rate
example - 	

Total bill amount is 30
number of people is 2
tip rate is 15

in command line type: 

>>>python tip.py 30 2 15
Amount: $30.00
People: 2.0
Tip Rate: 15.0%
The amount per person is: $17.25
				
Notes 
	Splits up a restaurtant check between people.
'''

#check he right amount 

def is_float(x):
	try:
		float(x)
		return True
	except Exception as e:
		return False	

def get_float(x, name):
	if not is_float(x):
		print name + " must be a number."
		sys.exit(1)
	return float(x)

if len(sys.argv) !=4:
	print PURPOSE
	sys.exit(1)

amount = get_float(sys.argv[1], "Amount")
people = get_float(sys.argv[2], "People")
tip_rate = get_float(sys.argv[3], "Tip Rate")

tip = amount * (tip_rate / 100.0)
tip_person = tip / people
amount_person = amount / people 
amount_person +=tip_person


print 'Amount: ${0:.2f}'.format(amount)
print 'People: {0}'.format(people)
print 'Tip Rate: {0}%'.format(tip_rate)
print 'The amount per person is: ${0:.2f}'.format(amount_person)