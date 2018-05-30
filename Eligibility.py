age = ""
name = ""

def eligibility(name,age):
	while True:
		name = input("Customer Name: ")
		try:
			age = int(input("Age: "))
			if age >= 18:
				print "Allowed"
			else:
				print "Sorry"
		except:
			print "Note: Please insert your age in numbers"
			
print eligibility(name,age)