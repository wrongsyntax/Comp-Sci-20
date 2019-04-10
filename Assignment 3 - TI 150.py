import PySimpleGUI  # Make sure to install PySimpleGUI before running with 'pip install pysimplegui' in a terminal

layout = [
    # For best results, please download the Digital-7 font from https://www.dafont.com/digital-7.font
    [PySimpleGUI.Input(size=(14, 1), do_not_clear=True, justification='right', key='input', font=('Digital-7', 45))],
    [PySimpleGUI.Text("Texas Instruments", font=('Helvetica', 15), text_color='black', justification='center',
                      background_color='white', relief=PySimpleGUI.RELIEF_RAISED)],
    [PySimpleGUI.Button('C'), PySimpleGUI.Button('CE'), PySimpleGUI.Button('%'), PySimpleGUI.Button('÷')],
    [PySimpleGUI.Button('7'), PySimpleGUI.Button('8'), PySimpleGUI.Button('9'), PySimpleGUI.Button('×')],
    [PySimpleGUI.Button('4'), PySimpleGUI.Button('5'), PySimpleGUI.Button('6'), PySimpleGUI.Button('-')],
    [PySimpleGUI.Button('1'), PySimpleGUI.Button('2'), PySimpleGUI.Button('3'), PySimpleGUI.Button('+')],
    [PySimpleGUI.Button('0'), PySimpleGUI.Button('.'), PySimpleGUI.Button('=', size=(25, 7))],
    [PySimpleGUI.Text('TI 150', size=(38, 1), text_color='black', font=('Helvetica', 13), justification='right')],
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
window = PySimpleGUI.Window(
    'TI 150',
    default_button_element_size=(11, 7),
    auto_size_buttons=False,
    grab_anywhere=False
).Layout(layout)

# Loop forever reading the window's values, updating the Input field
keys_entered = ''
operation = ''
while True:
    event, values = window.Read()  # read the window
    if event is None:  # if the X button clicked, just exit
        break
    if event == 'CE':  # clear keys if clear button
        keys_entered = ''
        first_val = ''
        answer = ''
        operation = ''
    elif event == 'C':
        keys_entered = keys_entered[:-1]
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
