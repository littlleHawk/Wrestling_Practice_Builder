# LIBRARIES
import pandas as pd


# GLOBALS

# Utility globals
SEED = 123
global VERBOSE
VERBOSE = True

# Padding time between moves
PADDING = 1

# Read in csv of moves
FILE_NAME = "./test_moves.csv"

# Supporting Utility Functions

def read_moves_list():
    df = pd.read_csv(FILE_NAME)
    if (VERBOSE):
        print("\nMOVES IN LIST")
        print("---------------------------------------------------")
        print(df)
    return df