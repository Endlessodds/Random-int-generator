import random
# Random is best module for generating Randomness.

num = random.randint(1, 170076)
     #module.module's function(start, end)

count = 0
# This count variable counts the number execution of the while loop.

while num>=4:
    print("ok")
    num = random.randint(1, 170076)
    # To escape the infinite while loop 
    count+=1
    # continues to print untill the num is <4
    # The count adds 1 everytime while loop is executed until it breaks the loop (when num is less than 4)

print(num)
# when loop breaks it prints the number.

print(f'{count}, times ')
# Final display for count
