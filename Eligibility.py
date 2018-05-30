age = ""                            # Passing Age as empty as we want it to work for various digits
name = ""                           # Passing Name as empty too

def eligibility(name,age):                             # Defining a procedure which accepts RAW value of name and age
	while True:                                    # While the condition is True
		name = input("Customer Name: ")        # input("") will let user type his name
		try:                                   # As we want age to be number not string we must create TRY, EXCEPT block
			age = int(input("Age: "))      # Now, (int(input("")) will let user type age, "int" will check if user typed digit
			if age >= 18:                  # We've criteria that if age is 18 or above then Customer is allowed
				print "Allowed"        # Print allowed in this case
			else:                          # If Customer is under 18 then "Sorry"
				print "Sorry"
		except:                                # Except will come into picture if user passes age as a "String" and not "Number"
			print "Note: Please insert your age in numbers"      # Print "Insert your age in name"
			
print eligibility(name,age)

# Once the code runs, it will prompt you to put "name" , pass the required name within "" (Quotes), e.g: "Gaurav"
# You can also try passing string in age to see what error you get.
