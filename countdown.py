import time
counter = 10

while counter > 0:
    print(counter)
    counter -= 1
    #We can include the time.sleep() to add a second in between in counting down to blast off
    #If we choose to comment it out, then it will print the descending order correctly.
    time.sleep(1)
print("Blast off!")
