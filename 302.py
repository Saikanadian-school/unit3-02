import ui
import random

number_to_guess = random.randint(1, 10)
print(number_to_guess)

def check_touch_up_inside(sender):
    
    number_entered = int(view['guess_textfield'].text)
    
    global number_to_guess
    if number_entered == number_to_guess:
        view['answer_label'].text = "You guessed correctly!"
    else:
        view['answer_label'].text = "Sorry, that is wrong. "
    
view = ui.load_view()
view.present('full_screen')
