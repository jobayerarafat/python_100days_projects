# if the bill was $159.00, split between 5 people, with 12% tip.

#each person sould pay (150.00 / 5)* 1.12+ 33.6

# round the reasult to 2 decimal places = 33.60

print("WELCOME TO THE TIP CALCULATOR !")
 
bill = float(input("What was the bill?\n $")) 
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
people =int(input("How many people to spit the bill?\n"))

bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_ammount = round(bill_per_person, 2)
final_ammount = "{:.2f}".format(bill_per_person)

print(f"Each person sould pay: ${final_ammount}")