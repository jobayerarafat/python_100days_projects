import random

letters = ['a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p','z','x','c','v','b','n','m',
           'Z','X','C','V','B','N','M','A','S','D','F','G','H','J','K','L','Q','W','E','R','T','Y','U','I','O','P']

numbers = ['1','2','3','4','5','6','7','8','9','0']

symbols = ['!','@','#','$','%','^','&','*','(',')','+','|','?']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols world you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list=[]

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
    
for char in range(1, nr_symbols + 1):
    password_list+= random.choice(symbols)
    
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)        
    
print(password_list)
random.shuffle(password_list)

password =""
for char in password_list:
    password += char    
    
print(f"Your password is : {password}")     