#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


#newlist = [expression for item in iterable if condition == True]
#new_list = [new_item for item in list]

#list comprehension
password_letters = [random.choice(letters) for items in range(nr_letters)]
#for this loop
#for char in range(nr_letters):
  #password_list.append(random.choice(letters))

#list comprehension
password_symbols = [random.choice(symbols) for items1 in range(nr_symbols)]
#for this loop
#for char in range(nr_symbols):
  #password_list += random.choice(symbols)

#list comprehension
password_numbers = [random.choice(numbers) for items2 in range(nr_numbers)]
#for this loop
#for char in range(nr_numbers):
  #password_list += random.choice(numbers)

password_list = password_numbers + password_letters + password_symbols

random.shuffle(password_list)

#this one
password = "".join(password_list)
#replace this loop
#password = ""
#for char in password_list:
  #password += char

print(f"Your password is: {password}")