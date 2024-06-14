import hashlib
import subprocess
import time

# Read Data For Data
f = open("PwnedPWs100k")
with open("PwnedPWs100k") as f:
    passwords = [line.rstrip('\n') for line in f]
f.close()

f = open("HashedPWs")
with open("HashedPWs") as f:
   hashed_pw = [line.rstrip('\n') for line in f]
f.close()

# Format User/Pw Data into Dict
hashed_pw_dict = {}
for line in hashed_pw:
    username, password = line.split(",")
    hashed_pw_dict[password] = username

def sha_hash(password):
    # Initializing the sha256() method
    sha256 = hashlib.sha256()
    # Passing the byte stream as an argument
    sha256.update(password.encode())
    # hexdigest() hashes the data, and returns
    # the output in hexadecimal format
    string_hash = sha256.hexdigest()
    return string_hash

def hash_lookup(hashed_pw):
    if hashed_pw in hashed_pw_dict:
        return True

def login(username, password):
    result = subprocess.run(["python3", "Login.pyc", username, password], capture_output = True, text = True)
    if result.stdout == "Login successful.\n":
        print(result.stdout.strip())
        print(f"Username '{username}': Password '{password}'")
        end = time.time()
        print(f"Time taken to find gang member: {end - start}")
        print()
        return True

def find_password():      
    for password in passwords:
        for digit1 in range(10):
            for digit2 in range(10):
                new_pw = password + str(digit1) + str(digit2)
                print(f'Attempting: {new_pw}')
                hashed_pw = sha_hash(new_pw)
                if hash_lookup(hashed_pw) == True:
                    username = hashed_pw_dict[hashed_pw]
                    if login(username, new_pw) == True:
                        return True
    return False

start = time.time()
print("Running Program")
print("Searching for passwords...")
print(f"\nProgram start time: {start - start}")

result = find_password()

if result == False:
    print("No Successful Login Attempts")

end = time.time()
print(f"\nProgram End Time: {end - start}")