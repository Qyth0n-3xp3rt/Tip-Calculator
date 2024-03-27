print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill: "))
tip = float(input("how much tip would you like to give: "))

end_tip = (bill*(tip/100)) + bill
total = round(end_tip, 2)

yn = str(input("Do you want to split the bill? "))
yn = yn.capitalize()
if yn == "Yes":
	yes = int(input("How much people do you want to split it with? "))
	yes = total/yes
	print(f"Each person has to pay {yes} dollars.")
elif yn == "No":
	print(f"The total bill is {total} dollars.")