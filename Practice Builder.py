#import random as rand
import utilities as u
import widgets_utilites as w
import datetime

# Call dataframe of moves
moves = u.read_moves_list()

time_dict = {"practice_length": w.practice_time,
             "warmup_time": w.warmup_time,
             "cooldown_time": w.cooldown_time,
             "live": w.live,
             "water_break": w.water_break,
             "padding": w.padding}

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

        self.moves_included = u.pd.DataFrame
    
    def info(self):
        print(f"{self.title} created on {self.date}: ")
        print(f"Length: {self.length}")
        print(f"Moves: {self.moves_included}")
#        print(f"Moves use {self.moves_include time / self.length * 100} % of practice")

time_dict = {"practice_time": w.practice_time,
             "warmup_time": w.warmup_time,
             "cooldown_time": w.cooldown_time,
             "live": w.live,
             "water_break": w.water_break,
             "padding": w.padding}

# build practice internal recursive function
def build_practice_recursor(temp_pract_time, pract_df):
    if(temp_pract_time <= 0):
        return pract_df
    # else, add to practice.


# Build a practice based on time alotted
# effectively main in this file
def build_practice(moves = moves):
    # Add widget for practice title
    # initialize practice
    time_used = (w.warmup_time +
                 w.cooldown_time +
                 w.live +
                 w. water_break)
    temp_pract_time = w.practice_time - time_used
    pract_df = u.pd.DataFrame





build_practice()


# Eviter calculaer plusier fois le meme system
# GPU Fuzzy check -> Frontier
#wrap Dash

dash = w.VBox([w.tau_slider, 
                w.alpha_slider,
                w.lifespan_estimation, 
            
                w.carbon_choice, 
                w.country_choice,
                w.listing_choice,
                w.sector_choice, 
                w.infos1, w.infos2, 
                w.infos3, w.infos4,
                w.outTotals])
                

#Show Dash
w.display(dash)
