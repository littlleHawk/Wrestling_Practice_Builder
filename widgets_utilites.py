
###################################################
#
#             INITIALIZE WIDGETS
#
###################################################
"""
Module for initializing the interactive widgets used in the dashboard.

"""
import ipywidgets as w
import utilities as u

# TODO
# Set JV and Varsity defaults
#defaults = {practice_time:}

# Get moves list
move_df = u.read_moves_list()

# WIDGETS TO CONTROL PRACTICE
# Intensity
intensity_slider = w.widgets.FloatSlider(value = 5.0, 
                                          min=0, max=10, step = 0.1,
                                          description='Intensity', 
                                          readout = True, 
                                          readout_format='.2f',
                                          continuous_update=False)


# choice of practice level
    # if Varsity, sets to varsity preset values
    # if JV, sets to JV preset values (longer breaks, more teaching time)
team_level = w.widgets.RadioButtons(
    options=['Varsity', 'JV'],
    value='Varsity',
    description='Practice Level',
    disabled=False)

#Move Selection
    # get lists for dropdowns
move_list = move_df['move'].unique().tolist()
move_list.sort()

move_choice = w.widgets.SelectMultiple(
    options= tuple(move_list),
    value= (),
    description='Moves',
    disabled=False)

warmup_time = w.widgets.BoundedFloatText(
    value = 20.0,
    min = 0.0,
    max = 35.0,
    step = 0.5,
    description = "Warmup Time",
    style={'description_width': 'initial'}
)

practice_time = w.widgets.BoundedFloatText(
    value = 120.0,
    min = 0.0,
    max = 180.0,
    step = 0.5,
    description = "Practice Time",
    style={'description_width': 'initial'}
)

cooldown_time = w.widgets.BoundedFloatText(
    value = 15.0,
    min = 0.0,
    max = 35.0,
    step = 0.5,
    description = "Cooldown Time",
    style={'description_width': 'initial'}
)

water_break = w.widgets.BoundedFloatText(
    value = 5.0,
    min = 0.0,
    max = 35.0,
    step = 0.5,
    description = "Water Break Time",
    style={'description_width': 'initial'}
)

live = w.widgets.BoundedFloatText(
    value = 0.0,
    min = 0.0,
    max = 120.0,
    step = 0.5,
    description = "Live Time",
    style={'description_width': 'initial'}
)

padding = w.widgets.BoundedIntText(
    value = 2.0,
    min  = 0.5,
    max = 10.0,
    step = 0.5,
    description = "Transition Padding",
    style={'description_width': 'initial'}
)

# TODO
# Add chained moves option
    # Radio button y/n
    # if yes, desplay all selected moves
    # allow user to drag moves into same hbox -> part of a chain
        # group these chains as tuples and calculate time as a chain


#"Add practice segments, will group moves my most similar
# and add a given amount of "teaching time" for each section"