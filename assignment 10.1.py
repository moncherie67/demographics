import os

demographics = input("Please enter a directory:  ")

if os.path.isdir(demographics):		
    print(f"directory already exists.")
else:
    os.mkdir(demographics)
    
user_demographics = input(f"Please provide your name: ")
user_demographics_2 = input(f"address:  ")
user_demographics_3 = input(f"phone number:  ")

with open(f'{demographics}/info.txt', 'w') as f: # f = open('test.txt, 'w')
    f.write(f"{user_demographics}, {user_demographics_2}, {user_demographics_3}")
    # f.close() 

with open(f'{demographics}/info.txt', 'r') as f:
    contents = f.read()
    print(contents)
 












    





