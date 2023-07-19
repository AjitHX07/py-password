import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z''A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

special_char = ['~', '!', '@', '#', '$', '%',
                '^', '&', '*', '(', ')', '_', '+', '-', '=']

print("welcome to pypassword manager")

letters_need = int(
    input("how many letters would you like in your passwords : "))

numbers_need = int(
    input("how many numbers would you like in your passwords : "))

special_char_need = int(input(
    "how many special charactors would you like in your passwords : "))

pass_list = []

for char in range(1, letters_need+1):
    gen_letters = random.choice(letters)
    pass_list += gen_letters

for num in range(1, numbers_need+1):
    gen_num = random.choice(numbers)
    pass_list += gen_num

for num in range(1, special_char_need+1):
    pass_list += random.choice(special_char)


random.shuffle(pass_list)


password = ""

for pass_loop in pass_list:

    password += pass_loop
print(f"Your password is : {password}")
