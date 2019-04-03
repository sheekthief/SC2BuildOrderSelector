import random
import buildorders


# Ask user what race they are ---
# Ask what the match up is ---
print("Welcome to Sheekthief's build order selector!")



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


BO_Selector()


# Ask if they want an econ build or all in or timing attack or random
# Probably random to start
# Clean up code and reduce repetition
