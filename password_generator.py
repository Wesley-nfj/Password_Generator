import random
import string

def password_gen(length):
    if length< 6:
      print("The length is too short. length should be no less than 6 characters ")
      return None
    else:
      password =""
      characters =string.ascii_letters + string.digits + string.punctuation
      for i in range(length):
       password = ''.join(random.choice(characters) for _ in range(length))
       return password


length= int(input("\n numner of characters of your password:\n "))
result= password_gen(length)
print(f"Your password is {result}")
