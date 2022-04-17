"""We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
We are in trouble if the parrot is talking and the hour is before 7 or after 20.
Return true if we are in trouble."""

current_hour = int(input("Enter hour: "))
if current_hour in range(7, 21):
    print("The party goes on!")
elif current_hour < 0 or current_hour > 24:
    print("You did not enter a valid hour")
else:
    print("We are in trouble!")
