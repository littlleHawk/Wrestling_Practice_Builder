
###################################################
#
#             INITIALIZE WIDGETS
#
###################################################
"""
Module for initializing the interactive widgets used in the dashboard.

"""
import ipywidgets as w
import pandas as pd
import utilities as u

# Get moves list
move_df  = pd.read_csv(u.FILE_NAME)


# build widgets to appear on dashboard
# Intensity
intensity_slider = w.widgets.FloatRangeSlider(value = [0, 10], 
                                          min=0, max=1, step = 0.01,
                                          description='Intensity', 
                                          readout = True, 
                                          readout_format='.2f',
                                          continuous_update=False)


# choice of dataset to use for electricity impact
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
    options= move_list,
    value= tuple(move_list['move'].unique().tolist()),
    description='Moves',
    disabled=False)


lifespan_estimation = w.widgets.BoundedFloatText(
    value = 5.0,
    min = 0.0,
    max = 35.0,
    step = 0.5,
    description = "Années après depassant le fond de la liste",
    style={'description_width': 'initial'},
)

