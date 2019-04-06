import PySimpleGUI as sg

layout = [
    [sg.Input(size=(14, 1), do_not_clear=True, justification='right', key='input', font=('Digital-7', 45))],
    [sg.Text("Texas Instruments", font=('Helvetica', 15), text_color='black', justification='center',
             background_color='white', relief=sg.RELIEF_RAISED)],
    [sg.Button('C'), sg.Button('CE'), sg.Button('%'), sg.Button('÷')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('×')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')],
    [sg.Button('0'), sg.Button('.'), sg.Button('=', size=(25, 7))],
    [sg.Text('', size=(21, 1), font=('Helvetica', 18), text_color='red', key='out'),
    sg.Text('TI 150', size=(5, 1), text_color='black', font=('Helvetica', 12))],
]


def percentify(number):
    number = float(number)
    return str(number/100)


def add(first, second):
    return float(first) + float(second)


def multiply(first, second):
    return float(first) * float(second)


def divide(first, second):
    return float(first) / float(second)


def subtract(first, second):
    return float(first) - float(second)


window = sg.Window(
    'TI 150',
    default_button_element_size=(11, 7),
    auto_size_buttons=False,
    grab_anywhere=False
).Layout(layout)

# Loop forever reading the window's values, updating the Input field
keys_entered = ''
while True:
    event, values = window.Read()  # read the window
    if event is None:  # if the X button clicked, just exit
        break
    if event == 'CE':  # clear keys if clear button
        keys_entered = ''
        first_val = ''
        answer = ''
        operation = ''
        window.FindElement('out').Update('')
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
            if float(keys_entered) != 0:
                answer = divide(first_val, keys_entered)
                keys_entered = answer
            else:
                keys_entered = "ERROR: Divide by 0"
        elif operation == '':
            keys_entered = keys_entered

    window.FindElement('input').Update(keys_entered)  # change the window to reflect current key string
