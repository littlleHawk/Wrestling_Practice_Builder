import random as rand
import pandas as pd

# GLOBALS
# All times in minutes
PRACT_TIME = 120
WARMUP_TIME = 20
COOLDOWN_TIME = 10
WATER_BREAK = 3
PADDING = 1
LIVE = False



# SUPPORTING FUNCTIONS
# Read in csv of moves
def read_file(filename):
    data = pd.read_csv(filename)
    print(data)

# gather input on practice parameters
def get_input():
    print("Current Assumptions: ")
    print(
        f"\tPRACT_TIME = {PRACT_TIME}\n",
        f"\tWARMUP_TIME = {WARMUP_TIME}\n",
        f"\tCOOLDOWN_TIME = {COOLDOWN_TIME}\n",
        f"\tWATER_BREAK = {WATER_BREAK}\n",
        f"\tPADDING = {PADDING}\n")
    change = input("Would you like to change any of this? (Y/n)")
    if (change== "Y" | change=="y"):
        # for each global ask for new value, or enter to retain current value
        print("Line 33 TODO")
    # Else contunye with following questions


# Build a practice based on time alotted
# effectively main in this file
def build_practice():
    read_file("test_moves.csv")
    get_input()

build_practice()
