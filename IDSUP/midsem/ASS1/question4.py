#Name : Priyansu Nagchowdhary
#Reg. no. : 2141014004
import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    try:
        password_length = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
        
        if password_length <= 0 or num_passwords <= 0:
            print("Please enter valid values for password length and number of passwords.")
            return
        
        print("Generated passwords:")
        for _ in range(num_passwords):
            password = generate_password(password_length)
            print(password)
    except ValueError:
        print("Please enter valid integers for password length and number of passwords.")

if __name__ == "__main__":
    main()
