#import random as rand
import pandas as pd
import ipywidgets as w
import utilities as u

# build practice internal recursive function
def build_practice_recursor(temp_pract_time, pract_df):
    if(temp_pract_time <= 0):
        return pract_df
    # else, add to practice.

# Build a practice based on time alotted
# effectively main in this file
def build_practice():
    read_file("test_moves.csv")
    time_used = WARMUP_TIME + COOLDOWN_TIME + WATER_BREAK + LIVE
    temp_pract_time = PRACT_TIME - time_used
    pract_df = pd.DataFrame




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
