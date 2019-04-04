import PySimpleGUI as sg

layout = [
    [sg.Text("Texas Instruments", font=('Helvetica', 22), text_color='black', justification='center',
             background_color='white', relief=sg.RELIEF_RAISED)],
    [sg.Input(size=(34, 44), do_not_clear=True, justification='left', key='input')],
    [sg.Button('C'), sg.Button('CE'), sg.Button('%'), sg.Button('÷')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('×')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')],
    [sg.Button('0'), sg.Button('.'), sg.Button('=')],
    [sg.Text('', size=(15, 1), font=('Helvetica', 18), text_color='red', key='out')],
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
    default_button_element_size=(7, 4),
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
            window.FindElement('out').Update(answer)  # output the final string
        elif operation == '-':
            answer = subtract(first_val, keys_entered)
            window.FindElement('out').Update(answer)
        elif operation == '×':
            answer = multiply(first_val, keys_entered)
            window.FindElement('out').Update(answer)
        elif operation == '÷':
            answer = divide(first_val, keys_entered)
            window.FindElement('out').Update(answer)
        keys_entered = ''

    window.FindElement('input').Update(keys_entered)  # change the window to reflect current key string
