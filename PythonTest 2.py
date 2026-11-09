import datetime

#If else test.
temperature = 50

if temperature <= 50:
    print ("Wear a jacket.")
else:
    print ("No jacket needed.")

#Pi test

import math
print(math.pi)

#For loop test (waterfall effect)
for ch in "hippopaunamonsterousquippedailephobia ":
    print(ch)

#Pi waterfall effect
for ch in str(math.pi):
    print(ch)

#Random test

print (datetime.time)

#if/elif/else test

coolness_points = 200

print(" ")

if coolness_points >= 5000:
    print("You are the coolest.")
elif coolness_points >= 2000:
    print("Coolness Rank: S++")
elif coolness_points >= 1000:
    print("Coolness Rank: S+")
elif coolness_points >= 975:
    print ("Coolness Rank: S")
elif coolness_points >= 925:
    print ("Coolness Rank: S-")
elif coolness_points >= 900:
    print ("Coolness Rank: A+")
elif coolness_points >=875:
    print ("Coolness Rank: A")
elif coolness_points >= 825:
    print ("Coolness Rank: A-")
elif coolness_points >= 800:
    print ("Coolness Rank: B+")
elif coolness_points >= 775:
    print ("Coolness Rank: B")
elif coolness_points >= 725:
    print ("Coolness Rank: B-")
elif coolness_points >= 700:
    print ("Coolness Rank: C+")
elif coolness_points >= 675:
    print ("Coolness Rank: C")
elif coolness_points >= 625:
    print ("Coolness Rank: C-")
elif coolness_points < 625:
    print ("You are not cool.")
elif coolness_points < 300:
    print ("""You're the opposite of "coolest" .""")