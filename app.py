import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model
model1 = load_model('loadtime.h5')
model2 = load_model('unloadtime.h5')

# Create dropdown menus for binary dummy variables
time_of_day_options = ['Morning', 'Early Afternoon', 'Late Afternoon', 'Night']
geofence_options = ['Atlanta', 'Austin', 'Baltimore',
       'Boston', 'Charlotte', 'Chicago',
       'Cincinnati', 'Cleveland',
       'Columbia', 'Columbus',
       'Dallas Fort Worth', 'Denver',
       'Detroit', 'Fairfield',
       'Fort Myers', 'Greenville',
       'Houston', 'Indianapolis',
       'Jacksonville', 'Kansas City',
       'Las Vegas', 'Long Island',
       'Louisville', 'Memphis', 'Miami',
       'Milwaukee', 'Minneapolis',
       'Nashville', 'North New Jersey',
       'Orlando', 'Philadelphia',
       'Phoenix', 'Port St. Lucie',
       'Providence', 'Richmond',
       'Riverside San Bernardino', 'Salt Lake City',
       'San Antonio', 'Sarasota',
       'Seattle', 'St. Louis', 'Tampa',
       'Virginia Beach', 'Washington DC',
       'Wichita']
partner_options = ['ArcBest', 'Best Buy',
       'Big Lots', 'EC Barton',
       'FedEx Freight', 'Floor & Decor',
       'GoLocal', 'OneRail',
       'Sherwin Williams', 'The Tile Shop']
service_level_options = ['First Threshold',
       'Fork-On / Fork-Off',
       'Room of Choice Ground Level',
       'Room of Choice Multi-Level',
       'Round Trip', 'White Glove']

st.set_page_config(layout="wide")
# Create the Streamlit app
st.title('Time Prediction using Neural Network')

# Create the tabs layout at the top of the page
tab1, tab2 = st.tabs(['Load Time','Unload Time'])

with tab1:
    st.title("Load Time")
    time_of_day1 = st.selectbox('Time of Day - Load', time_of_day_options)
    geofence1 = st.selectbox('Geofence - Load', geofence_options)
    partner1 = st.selectbox('Partner - Load', partner_options)

    # Convert the selected options to binary values
    variable1_binary1 = [1 if option == time_of_day1 else 0 for option in time_of_day_options]
    variable2_binary1 = [1 if option == geofence1 else 0 for option in geofence_options]
    variable3_binary1 = [1 if option == partner1 else 0 for option in partner_options]

    # Create the input data array
    test_instance1 = np.array([variable1_binary1 + variable2_binary1 + variable3_binary1])

    # Display the selected options and the predicted wait time
    if st.button('Make Load Time Prediction'):
        prediction1 = model1.predict(test_instance1)
        rounded_prediction1 = np.round(prediction1, decimals=1)
        st.write('Selected Options:', time_of_day1, geofence1, partner1)
        st.write('Predicted Load Time in Minutes:', rounded_prediction1[0][0])
with tab2:
    st.title("Unload Time")
    time_of_day2 = st.selectbox('Time of Day - Unload', time_of_day_options)
    geofence2 = st.selectbox('Geofence - Unload', geofence_options)
    partner2 = st.selectbox('Partner - Unload', partner_options)
    service_level = st.selectbox('Service Level', service_level_options)

    # Convert the selected options to binary values
    variable1_binary2 = [1 if option == time_of_day2 else 0 for option in time_of_day_options]
    variable2_binary2 = [1 if option == geofence2 else 0 for option in geofence_options]
    variable3_binary2 = [1 if option == partner2 else 0 for option in partner_options]
    variable4_binary2 = [1 if option == service_level else 0 for option in service_level_options]

    # Create the input data array
    test_instance2 = np.array([variable1_binary2 + variable2_binary2 + variable3_binary2 + variable4_binary2])

    # Display the selected options and the predicted wait time
    if st.button('Make Unload Time Prediction'):
        prediction2 = model2.predict(test_instance2)
        rounded_prediction2 = np.round(prediction2, decimals=1)
        st.write('Selected Options:', time_of_day2, geofence2, partner2, service_level)
        st.write('Predicted Unload Time in Minutes:', rounded_prediction2[0][0])



