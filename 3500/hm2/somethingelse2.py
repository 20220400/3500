import hashlib
import subprocess
import time


# Read Data For Data
f = open("PwnedPWs100k")
with open("PwnedPWs100k") as f:
   passwords = [line.rstrip('\n') for line in f]
f.close()


f = open("SaltedPWs")
with open("SaltedPWs") as f:
  salted_pws = [line.rstrip('\n') for line in f]
f.close()


f = open("gang")
with open("gang") as f:
  gang = [line.rstrip('\n') for line in f]
f.close()


# Format User/Pw Data into Dict
user_salt_dict = {}
user_pw_dict = {}
for line in salted_pws:
   user, salt, password  = line.split(",")
   user_salt_dict[user] = salt
   user_pw_dict[user] = password


def intersection(lst1, lst2):
   return list(set(lst1) & set(lst2))


def sha_hash(password):
   # Initializing the sha256() method
   sha256 = hashlib.sha256()
   # Passing the byte stream as an argument
   sha256.update(password.encode())
   # hexdigest() hashes the data, and returns
   # the output in hexadecimal format
   string_hash = sha256.hexdigest()
   return string_hash


def login(username, password):
   result = subprocess.run(["python3", "Login.pyc", username, password], capture_output = True, text = True)
   if result.stdout == "Login successful.\n":
       print(result.stdout.strip())
       print(f"Username '{username}': Password '{password}'")
       end = time.time()
       print(f"Time taken to find gang member: {end - start}")
       print()
       return True


def find_password(user):
   target_pw = user_pw_dict[user]
   salt = user_salt_dict[user]
   for password in passwords:
       for digit in range(10):
           new_pw = str(salt) + password + str(digit)
           new_pw1 = password + str(digit)
           print(f'Attempting: {new_pw}')
           hashed_pw = sha_hash(new_pw)
           if hashed_pw == target_pw:
               if login(user, new_pw1) == True:
                       return True
   return False


start = time.time()
print("Running Program")
print("Searching for passwords...")
print(f"\nProgram start time: {start - start}")


gang_members = list(user_salt_dict.keys())
login_status = False


the_gang = intersection(gang_members, gang)
for member in the_gang:
   if find_password(member) == True:
       login_status = True
       break


if login_status == False:
   print("No Successful Login Attempts")


end = time.time()
print(f"\nProgram End Time: {end - start}")


