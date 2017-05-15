current_dict = {}


def ask_user(choice):
    return input('Please, input your {}:\n'.format(choice))


# def collect_data():
#     return {ask_user('name'): ask_user('phone')}

# def check_existing(dict, name):
#     if dict[name]

while True:
    selector = input('''Please, select your choice:
"C"reate new
"R"ead existing
"U"pdate existing
"D"elete"
"Q"uit
                     ''').capitalize()
    if selector == "Q":
        break
    elif selector == "C":
        current_dict[ask_user('name')] = ask_user('phone')
    elif selector == "R":
        print(ask_user('name'))
    elif selector == "U":
        current_dict[ask_user('name')] = ask_user('phone')
    elif selector == "D":
        del current_dict[ask_user('name')]
    else:
        print('Input correct value!')

    print(current_dict)


