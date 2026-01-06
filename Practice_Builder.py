#import random as rand
import utilities as u
import widgets_utilites as w
import datetime

# Call dataframe of moves
moves = w.move_df

time_dict = {"practice_length": w.practice_time.value,
             "warmup_time": w.warmup_time.value,
             "cooldown_time": w.cooldown_time.value,
             "live": w.live.value,
             "water_break": w.water_break.value,
             "padding": w.padding.value}

#########################################################################################################

class practice:
    def __init__(self, title, time_dict):
        self.title = title
        self.date = datetime.datetime.now()
        self.length = time_dict["practice_length"]
        self.warmup_time = time_dict["warmup_time"]
        self.cooldown_time = time_dict["cooldown_time"]
        self.live = time_dict["live"]
        self.water_break = time_dict["water_break"]
        self.padding = time_dict["padding"]

        self.moves_included = u.pd.DataFrame(columns=["Move_Name",
                                                      "est_time",
                                                      "Repetitions",
                                                      "Linked"])
    
    def build_moves_df(self):
        self.moves_included
    
    def info(self):
        print(f"{self.title} created on {self.date}: ")
        print(f"Length: {self.length}")
        print(f"Moves: {self.moves_included}")
#        print(f"Moves use {self.moves_include time / self.length * 100} % of practice")
    
    def not_meat_potatatoes_time(self):
        return (self.warmup_time +
                self.cooldown_time + 
                self.live +
                self.water_break)
    
    def time_left(self):
        return (self.length - 
                self.not_meat_potatatoes_time()-
                self.moves_included["est_time"].sum())



#########################################################################################################

# build practice internal recursive function
def build_practice_recursor(temp_pract_time, practice_obj):
    if(temp_pract_time <= 0):
        return practice_obj
    # else, add to practice.
    if(u.VERBOSE):
        print(practice_obj.info())
        print("\nMoves_included: ")
        print(practice_obj.moves_included["Move_Name"].values)
    return


# Build a practice based on time alotted
# effectively main in this file
def build_practice(moves = moves):
    # Add widget for practice title
    # initialize practice
    practice_obj = practice("Test Practice", time_dict)
    build_practice_recursor(10, practice_obj)

build = w.w.interactive_output(build_practice())

