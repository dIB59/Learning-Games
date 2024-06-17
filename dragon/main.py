import random
import cave


def main():
    user_input = input("Which cave do you want to enter?")

    random_number = str(random.randint(0, 2))

    print(cave.enter(user_input, random_number))


if __name__ == "__main__":
    main()
