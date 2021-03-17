import random
words = ['anta',"nathan","bread","cake","apple","cave","event","letter","plugin","updates","windows","performance","hiring","filling","vlog","repair"]
def game_set_up():
    guessed_words=[]
    guessed_letters=[]
    fail_attempts = 5
    random_word = random.choice(words)
    answer = "-"*len(random_word)
    print("Welcome to hangman here are the rules:"
          "\n1.Goal of the game guess the word within 5 tries"
          "\n2.Only letters are allowed"
          "\n3.You are able to guess the word when ever you want. Note this does count as a guess if wrong"
          "\n4. Have fun!")
    while True:
        # end program there are 0 fail attempts or the answer becomes equal to the word.
        if fail_attempts==0 or answer==random_word:
            if fail_attempts==0:
                print(f"Sorry you have not guessed the word. The word was {random_word}.")
                break
            else:
                print(f"\nGreat job, you have found the word. You had {fail_attempts} fail_attempts left.")
                break
        guess=str(input("\nGuess a letter you think is in the word or try to guess the word: ").lower())
        if len(guess)==len(random_word):
            if guess==random_word:
                print(f"\nCongratulations, you got the answer the word was {random_word}")
                break
            else:
                if guess not in guessed_words:
                    guessed_words.append(guess)
                    fail_attempts-=1
                    print(f"\nSorry but is incorrect that is not the word. You have {fail_attempts} fail_attempts left.")
                else:
                    print(f"\nSorry but you have already guessed {guess}.")
        # checks if the guess is a valid answer(Valid answer=len is 1 is only letters)
        elif guess.isdigit()==True or guess.isalpha()==False or len(guess)!=1:
            fail_attempts-=1
            print(f"\nThat is a invalid guess.Please only enter one chacther or it is the same length as the word. Make sure they are only in the alphabet You now have {fail_attempts} guess")
        elif guess in guessed_letters:
            print("\n You have already guess that letter. Please choose a different letter")
        else:
            # Now snice guess is valid. Will now check if it's in the word.
            if guess in random_word:
                if random_word.count(guess)>1:
                    # checks if there are more than 1 occurrences in the word
                    for guess_letter in range(0,len(random_word)):
                        if guess == random_word[guess_letter]:
                            answer = answer[:guess_letter] + guess + answer[guess_letter + 1:]
                            if answer.count(guess)==random_word.count(guess):
                                guessed_letters.append(guess)
                                print(answer)
                    # if there is only 1 occurrences it just adds it
                else:
                    guessed_letters.append(guess)
                    answer=answer[:random_word.index(guess)] + guess + answer[random_word.index(guess)+ 1:]
                    print(answer)
                # if there is no occurrences in the word. It deducts 1 fail truy
            else:
                fail_attempts-=1
                guessed_letters.append(guess)
                print(f"\nSorry that is a {guess} is not in the world. You have {fail_attempts} left"
                      f"\n Here are the letters you have already guess!: {guessed_letters}")
def main():
    game_set_up()
main()
