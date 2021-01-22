# break keyword
# it is used when you have to terminate the running loop if you get the desired output
# this helps in stopping the code from unnecessary iterations

for i in range(11):
    print(i)
    if i == 5:
        break

# Continue keyword
# this helps in ignoring a satisfied condition and keeps the loop running
# the below code will check if the number is divisible by 2, it will break the iteration and continue with remaining loop
# hence it will print all the odd numbers
for i in range(11):
    if i % 2 == 0:
        continue
    print(i)