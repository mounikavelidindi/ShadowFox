import random

six_count = 0
one_count = 0
two_sixes = 0

previous = 0

for i in range(20):
    roll = random.randint(1, 6)

    print("Roll:", roll)

    if roll == 6:
        six_count += 1

    if roll == 1:
        one_count += 1

    if previous == 6 and roll == 6:
        two_sixes += 1

    previous = roll

print("Number of 6s:", six_count)
print("Number of 1s:", one_count)
print("Two 6s in a row:", two_sixes)