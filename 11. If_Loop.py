# IF loop
# indentation needs to be followed as python requires indentation while writing loops
# you can add multiple if and elif statement to the loop by following indentation
review = 3.5
if review > 4:
    print("The review is very good.")
elif review < 4 and review > 3:
    print("The review is good.")
elif review < 3 and review > 2:
    print("The review is average.")
else:
    print("The review is poor.")