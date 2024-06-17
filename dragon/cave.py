import render


def enter(user_input, number):
    if user_input == number:
        render.treasure()
    else:
        render.dragon()
