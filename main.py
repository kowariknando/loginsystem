# LOGIN SYSTEM
import csv

csvfile = csv.reader(open("users.csv"))
users = dict(csvfile)
#users = {'FERNANDO': '123', 'LUIS': '456', 'PACO': '789'}

print('Welcome to our Portal')
do_you_have_user = input('Do you have an user? Type YES to continue or NO to create a new user  ')
do_you_have_user = do_you_have_user.lower()
while do_you_have_user != 'yes' and do_you_have_user != 'no':
    print('please write yes or no')
    do_you_have_user = input('Do you have an user? Type yes to continue or no to create a new user  ')
    do_you_have_user = do_you_have_user.lower()
    continue
def create_user():
    new_user = input('please enter a user name  ')
    while new_user in users:
        print('this user already exist, please try again  ')
        new_user = input('please enter a user name  ')
        continue
    while new_user not in users:
        new_password = input('Please enter a password ')
        new_password2 = input('Please enter again your password  ')
        while new_password != new_password2:
            print('the passwords do not match!')
            new_password = input('Please enter a password  ')
            new_password2 = input('please enter again your password  ')
            continue
        users[new_user] = new_password
        print('Contratulations you have created succesfully a new User:  ', new_user)
        continue
def login_with_existing_user():
    print('Login with an existing registered USER')
    contador = 0
    while True:
        user_key = input('Please type your existing user:  ')
        if user_key in users:
            password = input('please enter your password')
            if users[user_key] == password:
                print('Your password is correct')
                break
            else:
                print('your password is not correct please try again')
                #print(contador)
                contador = contador + 1
                if contador == 3:
                    contador = 0
                    while True:
                        reply = input('you have failed many times, do you want to create a new user?  ')
                        if reply.lower() == 'yes':
                            create_user()
                            break
                        else:
                            break
        else:
            print('this user do not exist, please try again')
            contador = contador + 1
            if contador == 3:
                contador = 0
                while True:
                    reply = input('you have failed many times, do you want to create a new user?  ')
                    if reply.lower() == 'yes':
                        create_user()
                        break
                    else:
                        break


##CREATE NEW USER##
if do_you_have_user == 'no':
    print('lets create a new user')
    print(users)
    create_user()
    login_with_existing_user()
    print('WELCOME TO THE PORTAL')
    print('The current users are: ')
    print(users)

##ENTER WITH AN EXISTING USER##
if do_you_have_user == 'yes':
    login_with_existing_user()
    print('WELCOME TO THE PORTAL')
    print('The current users are: ')
    print(users)


with open('users.csv', 'w') as app_f:
    for key in users.keys():
        app_f.write("%s,%s\n" % (key, users[key]))

# TODO  crear un fichero en base al diccionario users que se abra y se salve en alg'un tipo de file .txt o lo que sea. Que se abra con un with open as
input('press enter to finish')