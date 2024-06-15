import random

def main():
    userInput: str = input("Which cave do you want to enter? (1 or 2)")
    
    number: int = random.randint(1, 2)
    
    print(enter_cave(userInput, number))

def enter_cave(userInput: str, number: int) -> str:
    if userInput == str(number):
        return("You have entered the cave with the treasure!")
    else:
        return("You have entered the cave with the dragon!")


if __name__ == "__main__":
    main()