import random
import string

def password_generator(n):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(n))
    return password


n = int(input("enter the length of password: "))
random_password = password_generator(n)
print(f"Random Password: {random_password}")
