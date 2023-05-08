"""

Pseudocode:

START
  PRINT "Hiking Tracker"

  input the number of days
  WHILE number of days is less than or equal to 0
    PRINT "Invalid number of days"
    input the number of days again

  SET total_distance to 0
  SET last_day_distance to 0

  FOR each day from 1 to the number of days
   input the distance for that day

    WHILE distance is greater than 120 or less than 0
      PRINT "Invalid distance"
      input the distance for that day again

    IF it is the last day
      SET last_day_distance to the current distance

    ADD the current distance to the total_distance

  CALCULATE the average distance by dividing total_distance by the number of days

  PRINT total distance
  PRINT average distance

  IF average distance is greater than the last day's distance
    PRINT "On your final day, your distance was below average."
  ELIF average distance is less than the last day's distance
    PRINT "On your final day, your distance was above average."
  ELSE
    PRINT "On your final day, your distance was the same as the average."

END



"""

print("Hiking Tracker")

day = int(input("Enter number of days: "))

while day <= 0:
    print("Invalid number of days")
    day = int(input("Enter number of days: "))

total_distance = 0
last_day_distance = 0

for d in range(day):
    distance = float(input(f"Day {d + 1} distance: "))

    while distance > 120 or distance < 0:
        print("Invalid distance")
        distance = float(input(f"Day {d + 1} distance: "))

    if d + 1 == day:
        last_day_distance = distance

    total_distance += distance

average = total_distance / day

print(f"Your total distance was: {total_distance} km")
print(f"Your average distance was: {average} km")
if average > last_day_distance:
    print(" On your final day, your distance was below average.")
elif average < last_day_distance:
    print("On your final day, your distance was above average.")
else:
    print("On your final day, your distance was the same as the average.")