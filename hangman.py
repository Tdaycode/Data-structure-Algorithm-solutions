import random

word_list = ['omotayo', 'lanre', 'maryam', 'camel', 'donkey'];

chosen_word = random.choice(word_list);


display = [];
for _ in range(len(chosen_word)):
    display += '_'
    print(display)

# user guess
end_of_game = False
while not end_of_game:
 user_guess = input('guess a letter :').lower();
 print(chosen_word)
 for position in range(len(chosen_word)):
    letter = chosen_word[position];
    if letter == user_guess:
        display[position] = letter;
print(display)

if '_' not in display:
    end_of_game = True
    print('You win')



