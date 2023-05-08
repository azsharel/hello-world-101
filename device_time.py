"""

Pseudocode:

START

input number of practices
input mow yes or no
if mow = yes and practices < 6
print you get said device time
elif mow = yes practices >= 7
print you get said device time + cupcake bonus
else no device time

END

"""

print("Device time determinator")
practices = int(input(" Number of practices? :"))
# did you mow?, Yes or No inputs.
mow = input("Did you mow?: ").lower()

if mow == "yes" and practices < 6:
    print(f"You get { practices * 15} minutes of device time :) ")
elif mow == "yes" and practices >= 7:
    print(f"You get { practices * 15} minutes of device time :) ")
    print("AND you get a cupcake :)")
else:
    print("no device time :( ")






