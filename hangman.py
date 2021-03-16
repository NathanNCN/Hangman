import random
words = ['anta',"nathan","bread","cake","apple","cave","event","letter","plugin","updates","windows","performance","hiring","filling","vlog","repair"]
def game_set_up():
    guessed_words=[]
    guessed_letters=[]
    guesses = 5
    random_word = random.choice(words)
    answer = "-"*len(random_word)
    print("Welcome to hangman here are the rules:"
          "\n1.Goal of the game guess the word within 5 tries"
          "\n2.Only letters are allowed"
          "\n3.You are able to guess the word when ever you want. Note this does count as a guess if wrong"
          "\n4. Have fun!")
    while True:
        if guesses==0:
            print(f"Sorry you have not guessed the word. The word was {random_word}.")
        if answer==random_word:
            print(f"\nGreat job, you have found the word. You had {guesses} guesses left.")
            break
        guess=str(input("\nGuess a letter you think is in the word or try to guess the word: ").lower())
        if len(guess)==len(random_word):
            if guess==random_word:
                print(f"\nCongratulations, you got the answer the word was {random_word}")
            elif guess!=random_word:
                if guess not in guessed_words:
                    guessed_words.append(guess)
                    guesses-=1
                    print(f"\nSorry but is incorrect that is not the word. You have {guesses} guesses left.")
                else:
                    print(f"\nSorry but you have already guessed {guess}.")
        elif guess.isdigit()==True or guess.isalpha()==False or len(guess)!=1:
            guesses-=1
            print(f"\nThat is a invalid guess.Please only enter one chacther or it is the same length as the word. Make sure they are only in the alphabet You now have {guesses} guess")
        elif guess in guessed_letters:
            print("\n You have already guess that letter. Please choose a different letter")
        else:
            if guess in random_word:
                if random_word.count(guess)>1:
                    for guess_letter in range(0,len(random_word)):
                        if guess == random_word[guess_letter]:
                            answer = answer[:guess_letter] + guess + answer[guess_letter + 1:]
                            if answer.count(guess)==random_word.count(guess):
                                guessed_letters.append(guess)
                                print(answer)
                else:
                    guessed_letters.append(guess)
                    answer=answer[:random_word.index(guess)] + guess + answer[random_word.index(guess)+ 1:]
                    print(answer)
            elif guess not in random_word:
                guesses-=1
                guessed_letters.append(guess)
                print(f"\nSorry that is a {guess} is not in the world. You have {guesses} left"
                      f"\n Here are the letters you have already guess!: {guessed_letters}")
def main():
    game_set_up()

main()

