import random

words = [
    "alphacode", "internship", "developer", "mogger",
    "sigma", "warbringers", "database", "network",
    "howlers", "freefire", "neural network", "syntax"
]

word = random.choice(words)
blanks = ['_'] * len(word)
chances = 3
print("🎮 Welcome to Hangman (Tech Edition) THE TOUGHEST VERSION\n")

while chances > 0:
    print("\nWord:", " ".join(blanks))
    guess = input("Enter a letter: ").lower()

   
    if len(guess) != 1:
        print("Enter ONLY one letter.JUST HOLD ON TIGHT")
        continue

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                blanks[i] = guess
    else:
        chances -= 1
        print("❌ Wrong! Chances left:", chances)

    # win condition
    if '_' not in blanks:
        print("\n🎉 YOU WIN!chill man you have just won  & The word was:", word)
        break

# lose condition
if chances == 0:
    print("\n💀 YOU LOSE!dont try again &The word was:", word)