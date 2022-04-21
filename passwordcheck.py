name = input("Enter the name")
passwordd = input("Enter the password")
password_length = len(passwordd)
hide_passwordd = password_length * '*'
print(f'hey {name} , your password {hide_passwordd} is this much long {password_length}')
