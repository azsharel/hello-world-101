"""

Pseudocode:

START
print "Warm pizza pay calculator"
input number of trips
input number of minutes
trip_ pay = trips * 1.45
min_pay = minutes * 0.95
total pay = trip_pay + min_pay
print trips in pay
print minutes in pay
print total_pay
END

"""
print("Warm Pizza pay calculator")
trips = float(input("Enter Number of trips: "))
minutes = float(input("Enter number of minutes: "))
# $1.45 is the pay rate per trip.
trip_pay = trips * 1.45
# $0.95 is the pay rate per minute.
min_pay = minutes * 0.95
print(f"for {trips} trips your pay is ${trip_pay}" )
print(f"for {minutes} minutes your pay is ${min_pay} ")
print(f"your total pay is: {trip_pay + min_pay} ")

