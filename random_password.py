from random import choice

len_of_password = 8
valid_character_for_password = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$&_+*@+=%?0123456789"

password = []

for each_char in range(len_of_password):
    password.append(choice(valid_character_for_password))
new_password = "".join(password)
print(new_password)