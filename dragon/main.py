import random

def main():
    userInput: str = input("Which cave do you want to enter? (1 or 2)")
    
    number: int = random.randint(1, 2)
    
    if userInput == str(number):
        print("You have entered the cave with the treasure!")
    else:
        print("You have entered the cave with the dragon!")


if __name__ == "__main__":
    main()