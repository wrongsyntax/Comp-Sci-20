import PySimpleGUI as sg  # Make sure to install PySimpleGUI before running with 'pip install pysimplegui' in a terminal

layout = [
    # For best results, please download the Digital-7 font from https://www.dafont.com/digital-7.font
    [sg.Input(size=(16, 1), do_not_clear=True, justification='right', key='input', font=('Digital-7', 45),
              text_color='darkorange')],
    [sg.Text("Texas Instruments", font=('Helvetica', 15), text_color='black', justification='center',
             background_color='white', relief=sg.RELIEF_RAISED)],
    [sg.Button('C', font="Ariel 20"), sg.Button('CE', font="Ariel 20"), sg.Button('%', font="Ariel 20"),
     sg.Button('÷', font="Ariel 20")],
    [sg.Button('7', font="Ariel 20"), sg.Button('8', font="Ariel 20"), sg.Button('9', font="Ariel 20"),
     sg.Button('×', font="Ariel 20")],
    [sg.Button('4', font="Ariel 20"), sg.Button('5', font="Ariel 20"), sg.Button('6', font="Ariel 20"),
     sg.Button('-', font="Ariel 20")],
    [sg.Button('1', font="Ariel 20"), sg.Button('2', font="Ariel 20"), sg.Button('3', font="Ariel 20"),
     sg.Button('+', font="Ariel 20")],
    [sg.Button('0', font="Ariel 20"), sg.Button('.', font="Ariel 20"), sg.Button('=', font="Ariel 20", size=(13, 4))],
    [sg.Text('TI 150', size=(44, 1), text_color='black', font=('Helvetica', 13), justification='right')],
]


def percentify(number):
    try:
        number = float(number)
        return str(number/100)
    except ValueError:
        return "ERROR"


def add(first, second):
    try:
        return float(first) + float(second)
    except ValueError:
        return "ERROR"


def multiply(first, second):
    try:
        return float(first) * float(second)
    except ValueError:
        return "ERROR"


def divide(first, second):
    try:
        return float(first) / float(second)
    except ValueError:
        return "ERROR"


def subtract(first, second):
    try:
        return float(first) - float(second)
    except ValueError:
        return "ERROR"


# Initialize the window
window = sg.Window(
    'TI 150',
    default_button_element_size=(6, 4),
    auto_size_buttons=False,
    grab_anywhere=False
).Layout(layout)

# Loop forever reading the window's values, updating the Input field
keys_entered = ''
operation = ''
first_val = ''
while True:
    event, values = window.Read()  # read the window
    if event is None:  # if the X button clicked, just exit
        break
    if event == 'CE':  # clear keys if clear button
        keys_entered = ''
        first_val = ''
        answer = ''
        operation = ''
    elif event == 'C':  # backspace button
        keys_entered = keys_entered[:-1]  # removes last character of the string
    elif event == '%':
        keys_entered = percentify(keys_entered)
    elif event in '1234567890.':
        keys_entered = values['input']  # get what's been entered so far
        keys_entered += event  # add the new digit
    elif event == '+':
        first_val = keys_entered
        keys_entered = ''
        operation = '+'
    elif event == '-':
        first_val = keys_entered
        keys_entered = ''
        operation = '-'
    elif event == '×':
        first_val = keys_entered
        keys_entered = ''
        operation = '×'
    elif event == '÷':
        first_val = keys_entered
        keys_entered = ''
        operation = '÷'
    elif event == '=':
        keys_entered = values['input']
        if operation == '+':
            answer = add(first_val, keys_entered)
            keys_entered = answer
        elif operation == '-':
            answer = subtract(first_val, keys_entered)
            keys_entered = answer
        elif operation == '×':
            answer = multiply(first_val, keys_entered)
            keys_entered = answer
        elif operation == '÷':
            try:
                if float(keys_entered) != 0:
                    answer = divide(first_val, keys_entered)
                    keys_entered = answer
                else:
                    keys_entered = "ERROR: Divide by 0"
            except ValueError:
                keys_entered = "ERROR"
        elif operation == '':
            keys_entered = keys_entered

    window.FindElement('input').Update(keys_entered)  # change the window to reflect current key string
