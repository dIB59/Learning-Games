import render

def check_answer(answer):
      
    correct_answers = ["42", "forty-two", "forty two"]

    # .string will remove leading and trailing whitespaces 
    # .lower will convert the string to lowercase this ensures that the comparison is case-insensitive
    if answer.strip().lower() in correct_answers:
        render.render_correct()
        return "Yes, 42 is indeed the answer to the ultimate question of life, the universe, and everything!"
    else:
        render.render_incorrect()
        return "Incorect answer human"

def main():
    print("In 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams,")
    print("a supercomputer named Deep Thought determines the answer to the ultimate question of life, the universe, and everything ")
    user_answer = input("Can you guess what is the answer to the Great Question of Life, the Universe, and Everything?  ")
    print(check_answer(user_answer))

if __name__ == "__main__":
    main()
