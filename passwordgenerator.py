import random

letters = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z'];
numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9'];
symbols = ['!', '>', '<', '%', '&', '@', '#', '$', '*','^','~','+']


print('Welcome to Pypasssword Generator');
nr_letters =int(input(f'How many letters would you like your password?\n'));
nr_symbols =int(input(f'How many symbols would you like your password?\n'));
nr_numbers =int(input(f'How many numbers would you like your password?\n'));

rd_letters = random.sample(letters, nr_letters);
rd_symbols = random.sample(symbols, nr_symbols);
rd_numbers = random.sample(numbers, nr_numbers);

rand_sum = rd_letters + rd_numbers + rd_symbols;
re_arrange = random.sample(rand_sum, len(rand_sum))
rand_password = ''
print(f'your generated password is : {rand_password.join(re_arrange)}')
       



