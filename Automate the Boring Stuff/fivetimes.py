# Practicing for loops
# 31/10/2023

# Printing the name five times using a for loop.

print('My name is')
for i in range(5):
    print('Ryan Five TImes (' + str(i) + ')')

# Adding all the numbers between 1 - 100 with a for loop.

total = 0

for num in range(101):
    total = total + num

print (total)

# Acheiving the same output with a while loop.

print('My name is')

i = 0

while i < 5:
    
    print('Jimmy Five Times (' + str(i) + ')')

    i = i + 1

for i in range(0, 10, 2):
    print(i)