secretWord = "Python"

num_tries = 0
guess = ""

while guess != secretWord and num_tries<3:

	guess = input("Guess the secret word: ")
	num_tries += 1
	
if guess == secretWord:

	print ("You guessed correct!")
elif num_tries == 3:
	print("Sorry, you've made 3 unsuccessful attempts!")