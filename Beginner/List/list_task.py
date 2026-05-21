justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

print(justice_league)

# 1
print("Members:", len(justice_league))

# 2
justice_league.append("Batgirl")
justice_league.append("Nightwing")

print(justice_league)

# 3
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print(justice_league)

# 4
justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")

print(justice_league)

# 5
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]

print(justice_league)

# 6
justice_league.sort()

print(justice_league)
print("New Leader:", justice_league[0])