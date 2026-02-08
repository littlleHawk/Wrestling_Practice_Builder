#import random as rand
import utilities as u
import widgets_utilites as w
import datetime

# Call dataframe of moves
moves_df = w.move_df

# Note: #! Indicates somewhere the user could input their own values 
# to optimize hardcode sections
#
#
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
        print(f"Non-Move time: {self.warmup_time+self.cooldown_time+self.live}")
        print(f"Moves: {self.moves_included}")
#        print(f"Moves use {self.moves_include time / self.length * 100} % of practice")
    
    def not_meat_potatatoes_time(self):
        return (self.warmup_time +
                self.cooldown_time + 
                self.live +
                self.water_break)
    
    def padding_total(self):
        return self.padding * len(self.moves_included)
    
    def time_left(self):
        return (self.length - 
                self.not_meat_potatatoes_time()-
                self.moves_included["est_time"].sum()-
                self.padding_total())
    
    def display_practice_timeline(self, set_length = 10):
        for i in range(len(self.moves_included)):
            move = self.moves_included.iloc[i]
            reps = move["Repetitions"]
            rep_counter = 0
            for rep in range(reps):
                if (rep % set_length == 0) and rep != 0:
                    print(f"{move['Move_Name']}: {set_length} reps")
                    print(f"Padding/Transition time: {w.padding.value} minutes")
                rep_counter += 1
            print("=========================================")



#########################################################################################################

# Set initial warmup values
#! Change these as you see fit for JV/Varsity Presets
def update_presets(change):
    level = change['new']
    
    if level == "JV":
        w.practice_time.value = 120
        w.warmup_time.value = 15
        w.live.value = 10
        w.intensity_slider.value = 3
        w.cooldown_time.value = 10
        w.live.value = 0
        w.water_break.value = 5
        w.padding.value = 3
    elif level == "Varsity":
        w.practice_time.value = 120
        w.warmup_time.value = 20
        w.live.value = 6
        w.intensity_slider.value = 7
        w.cooldown_time.value = 10
        w.water_break.value = 2
        w.padding.value = 2

# Link the team_level widget to this function
w.team_level.observe(update_presets, names='value')

#########################################################################################################

# build practice internal recursive function
# def build_practice_recursor(temp_pract_time, practice_obj):
#     if(temp_pract_time <= 0):
#         return practice_obj
#     # else, add to practice.
#         # Could be implemented in a binary search tree
    

#     # Print progress messages if verbose

#     # Print final move list message if verbose
#     if(u.VERBOSE):
#         print(practice_obj.info())
#         print("\nMoves_included: ")
#         print(practice_obj.moves_included["Move_Name"].values)
#     return


# Build a practice based on time alotted
# effectively main in this file
def build_practice(verbose = False):
    # Get practice title
    input_title = w.practice_title.value
    # If no title, create one with date and time
    if input_title == "":
        input_title = "Practice" + "_" + datetime.datetime.today().strftime("%Y-%m-%d_%H-%M")

    # Get current widget values
    time_dict = {"practice_length": w.practice_time.value,
             "warmup_time": w.warmup_time.value,
             "cooldown_time": w.cooldown_time.value,
             "live": w.live.value,
             "water_break": w.water_break.value,
             "padding": w.padding.value}
    # Get move list
    moves_list = list(w.move_choice.value)
    # if no moves selected, return empty practice
    if len(moves_list) == 0:
        print("No moves selected, returning empty practice")
        return practice("Empty Practice", time_dict)
   
    # initialize practice
    practice_obj = practice(input_title, time_dict)
    #build_practice_recursor(10, practice_obj)
    # DEBUGGING PRINTS
    if verbose:
        print(practice_obj.info())

    while practice_obj.time_left() > 0:
        # Get each move in list of moves selected
        for move in moves_list:
            # For each move, add a reasonable number of sets and reps, with padding between each set
            est_time = (moves_df[moves_df["move"] == move]["est_time"].values[0]) / 60 # convert to minutes
            # Until the time left is less than 0, at which point, stop adding moves and return practice object
            if practice_obj.time_left() - est_time > 0:
                repetitions = int(practice_obj.time_left() / est_time / len(moves_list))

                practice_obj.moves_included = u.pd.concat(
                        [practice_obj.moves_included,
                            u.pd.DataFrame([{
                                "Move_Name": move,
                                "est_time": est_time * repetitions,
                                "Repetitions": repetitions,
                                "Linked": False}])], ignore_index=True
                                )
                # add padding time based on number of reps, with 1 padding unit per 10 reps
                practice_obj.padding = w.padding.value * (repetitions/10) 
            else:
                if verbose:
                    print(f"Time left: {practice_obj.time_left()}, not adding move: {move}")
                # Format move datafame
                practice_obj.moves_included = practice_obj.moves_included.groupby("Move_Name").agg({"est_time": "sum", "Repetitions": "sum", "Linked": lambda x: tuple(x)}).reset_index()
                return practice_obj

    # Return practice object if the while loop doesn't
    return(practice_obj)

def export_practice(practice_obj):
    filename = practice_obj.title + ".txt"
    with open(filename, 'w') as f:
        f.write(f"{practice_obj.title} created on {practice_obj.date}: \n")
        f.write(f"Length: {practice_obj.length}\n")
        f.write(f"Non-Move time: {practice_obj.not_meat_potatatoes_time()}\n")
        f.write("Moves:\n")
        for index, row in practice_obj.moves_included.iterrows():
            f.write(f"{row['Move_Name']}: {row['Repetitions']} reps, est time: {row['est_time']} minutes\n")
        f.write(f"Moves use {practice_obj.moves_included['est_time'].sum() / practice_obj.length * 100} % of practice\n")
    print(f"Practice exported to {filename}")

#########################################################################################################
# Display practice

# Create a dedicated output 

output_window = w.w.Output()

def on_button_clicked(b):
    # Clear previous practice before printing new one
    output_window.clear_output()

    with output_window:
        pract = build_practice(verbose=False)
        # TODO: Format this output better, maybe with HTML and CSS?
        print(f"\n{pract.title}:")
        pract.info()
        pract.display_practice_timeline()

# Link the button to the function
w.generate_button.on_click(on_button_clicked)


