from random import choice
import random
from builds import builds

def BuildOrder():
    build = None
    while build is None:
        matchup = input("What is the matchup? ").upper()
        if matchup not in builds:
            print("Invalid Input, try again.")
            continue

        build = random.choice(builds[matchup])
        print(matchup + " Build Order:")
        print(build)


"""
Code grabbed from reddit to help me along!


def BO_Selectorv2():
    build = None
    while build is None:
        matchup = input("What is the matchup? ").upper()
        if matchup not in builds:
            print("Invalid Input, try again.")
            continue
        build = (random.choice(builds[str(matchup)]))
    print('{matchup) Build Order:')
    print(build)
"""

"""
Original Build Order Selector!

def BO_Selector():

    matchup = input("What is the matchup? ")
    if matchup.upper() == "ZVP":
        print("ZvP Build Order: ")
        build = random.choice(buildorders.zvp_build_orders)
        print(build)
        BO_Selector()
    elif matchup.upper() == "ZVT":
        print("ZvT Build Order: ")
        build = random.choice(buildorders.zvt_build_orders)
        print(build)
        BO_Selector()
    elif matchup.upper() == "ZVZ":
        print("ZvZ Build Order: ")
        build = random.choice(buildorders.zvz_build_orders)
        print(build)
        BO_Selector()
    elif matchup.upper() == "PVP":
        print("PvP Build Order: ")
        build = random.choice(buildorders.pvp_build_orders)
        print(build)
        BO_Selector()
    elif matchup.upper() == "PVT":
        print("PvT Build Order: ")
        build = random.choice(buildorders.pvt_build_orders)
        print(build)
        BO_Selector()
    elif matchup.upper() == "PVZ":
        print("PvZ Build Order: ")
        build = random.choice(buildorders.pvz_build_orders)
        print(build)
        BO_Selector()
    elif matchup.upper() == "TVP":
        print("TvP Build Order: ")
        build = random.choice(buildorders.tvp_build_orders)
        print(build)
        BO_Selector()
    elif matchup.upper() == "TVT":
        print("TvT Build Order: ")
        build = random.choice(buildorders.tvt_build_orders)
        print(build)
        BO_Selector()
    elif matchup.upper() == "TVZ":
        print("TvZ Build Order: ")
        build = random.choice(buildorders.tvz_build_orders)
        print(build)
        BO_Selector()
    else:
        print("Invalid Input, try again.")
        BO_Selector()

"""

print("Welcome to Sheekthief's build order selector!")
BuildOrder()

