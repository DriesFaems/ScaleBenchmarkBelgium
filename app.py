import pandas as pd
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# read pickle

fulldata = pd.read_pickle('Full data with Scalers, High Growth Firms and Consistent High Growth Firms.pkl')

# greate variable percentage of scalers 2021
scaler2021 = list(fulldata['Scaler 2021'])
percentage_scalers_2021 = scaler2021.count(1)/(scaler2021.count(0)+scaler2021.count(1))*100
number_scalers_2021 = scaler2021.count(1)

# create variable percentage of scalers 2022
scaler2022 = list(fulldata['Scaler 2022'])
percentage_scalers_2022 = scaler2022.count(1)/(scaler2022.count(0)+scaler2022.count(1))*100
number_scalers_2022 = scaler2022.count(1)

# create variable percentage of scalers 2020
scaler2020 = list(fulldata['Scaler 2020'])
percentage_scalers_2020 = scaler2020.count(1)/(scaler2020.count(0)+scaler2020.count(1))*100
number_scalers_2020 = scaler2020.count(1)

# create variable percentage of scalers 2019
scaler2019 = list(fulldata['Scaler 2019'])
percentage_scalers_2019 = scaler2019.count(1)/(scaler2019.count(0)+scaler2019.count(1))*100
number_scalers_2019 = scaler2019.count(1)

# create variable percentage of scalers 2018
scaler2018 = list(fulldata['Scaler 2018'])
percentage_scalers_2018 = scaler2018.count(1)/(scaler2018.count(0)+scaler2018.count(1))*100
number_scalers_2018 = scaler2018.count(1)

# greate variable percentage of highgrowth 2021
highgrowth2021 = list(fulldata['HighGrowthFirm 2021'])
percentage_highgrowth_2021 = highgrowth2021.count(1)/(highgrowth2021.count(0)+highgrowth2021.count(1))*100
number_highgrowth_2021 = highgrowth2021.count(1)

# create variable percentage of highgrowth 2022
highgrowth2022 = list(fulldata['HighGrowthFirm 2022'])
percentage_highgrowth_2022 = highgrowth2022.count(1)/(highgrowth2022.count(0)+highgrowth2022.count(1))*100
number_highgrowth_2022 = highgrowth2022.count(1)

# create variable percentage of highgrowth 2020
highgrowth2020 = list(fulldata['HighGrowthFirm 2020'])
percentage_highgrowth_2020 = highgrowth2020.count(1)/(highgrowth2020.count(0)+highgrowth2020.count(1))*100
number_highgrowth_2020 = highgrowth2020.count(1)

# create variable percentage of highgrowth 2019
highgrowth2019 = list(fulldata['HighGrowthFirm 2019'])
percentage_highgrowth_2019 = highgrowth2019.count(1)/(highgrowth2019.count(0)+highgrowth2019.count(1))*100
number_highgrowth_2019 = highgrowth2019.count(1)

# create variable percentage of highgrowth 2018
highgrowth2018 = list(fulldata['HighGrowthFirm 2018'])
percentage_highgrowth_2018 = highgrowth2018.count(1)/(highgrowth2018.count(0)+highgrowth2018.count(1))*100
number_highgrowth_2018 = highgrowth2018.count(1)

# create variable percentage of consistent highgrowth 2021
consistenthighgrowth2021 = list(fulldata['ConsistentHighGrowthFirm 2021'])
percentage_consistenthighgrowth_2021 = consistenthighgrowth2021.count(1)/(consistenthighgrowth2021.count(0)+consistenthighgrowth2021.count(1))*100
number_consistenthighgrowth_2021 = consistenthighgrowth2021.count(1)

# create variable percentage of consistent highgrowth 2022
consistenthighgrowth2022 = list(fulldata['ConsistentHighGrowthFirm 2022'])
percentage_consistenthighgrowth_2022 = consistenthighgrowth2022.count(1)/(consistenthighgrowth2022.count(0)+consistenthighgrowth2022.count(1))*100
number_consistenthighgrowth_2022 = consistenthighgrowth2022.count(1)

# create variable percentage of consistent highgrowth 2020
consistenthighgrowth2020 = list(fulldata['ConsistentHighGrowthFirm 2020'])
percentage_consistenthighgrowth_2020 = consistenthighgrowth2020.count(1)/(consistenthighgrowth2020.count(0)+consistenthighgrowth2020.count(1))*100
number_consistenthighgrowth_2020 = consistenthighgrowth2020.count(1)

# create variable percentage of consistent highgrowth 2019
consistenthighgrowth2019 = list(fulldata['ConsistentHighGrowthFirm 2019'])
percentage_consistenthighgrowth_2019 = consistenthighgrowth2019.count(1)/(consistenthighgrowth2019.count(0)+consistenthighgrowth2019.count(1))*100
number_consistenthighgrowth_2019 = consistenthighgrowth2019.count(1)

# create variable percentage of consistent highgrowth 2018
consistenthighgrowth2018 = list(fulldata['ConsistentHighGrowthFirm 2018'])
percentage_consistenthighgrowth_2018 = consistenthighgrowth2018.count(1)/(consistenthighgrowth2018.count(0)+consistenthighgrowth2018.count(1))*100
number_consistenthighgrowth_2018 = consistenthighgrowth2018.count(1)

# input company name

st.title("ESI Benchmarking Tool Belgium")

st.write("This tool allows to benchmark particular regions and/or industries in terms of scaling companies.")

# generate in streamlit a dropdown menu with all the countries

countries = fulldata['Region in country'].unique()
countries = np.insert(countries, 0, 'all')
country = st.selectbox('Select a region', countries)

#generat in streamlist a dropdown menu with all the industries

industries = fulldata['BvD sectors'].unique()
industries = np.insert(industries, 0, 'all')
industry = st.selectbox('Select an industry', industries)

clicked = st.button('Click me')

if clicked:
    if country == 'all' and industry == 'all':
        selectdata = fulldata
    elif country == 'all':
        selectdata = fulldata[fulldata['BvD sectors'] == industry].reset_index(drop=True)
    elif industry == 'all':
        selectdata = fulldata[fulldata['Region in country'] == country].reset_index(drop=True)
    else:
        selectdata = fulldata[(fulldata['Region in country'] == country) & (fulldata['BvD sectors'] == industry)].reset_index(drop=True)
    selectscaler2021 = list(selectdata['Scaler 2021'])
    selectpercentage_scaler_2021 = selectscaler2021.count(1)/(selectscaler2021.count(0)+selectscaler2021.count(1))*100
    selectnumber_scaler_2021 = selectscaler2021.count(1)

    selectscaler2022 = list(selectdata['Scaler 2022'])
    selectpercentage_scaler_2022 = selectscaler2022.count(1)/(selectscaler2022.count(0)+selectscaler2022.count(1))*100
    selectnumber_scaler_2022 = selectscaler2022.count(1)

    selectscaler2020 = list(selectdata['Scaler 2020'])
    selectpercentage_scaler_2020 = selectscaler2020.count(1)/(selectscaler2020.count(0)+selectscaler2020.count(1))*100
    selectnumber_scaler_2020 = selectscaler2020.count(1)

    selectscaler2019 = list(selectdata['Scaler 2019'])
    selectpercentage_scaler_2019 = selectscaler2019.count(1)/(selectscaler2019.count(0)+selectscaler2019.count(1))*100
    selectnumber_scaler_2019 = selectscaler2019.count(1)

    selectscaler2018 = list(selectdata['Scaler 2018'])
    selectpercentage_scaler_2018 = selectscaler2018.count(1)/(selectscaler2018.count(0)+selectscaler2018.count(1))*100
    selectnumber_scaler_2018 = selectscaler2018.count(1)
    
    percentage_scalers_2021 = round(percentage_scalers_2021, 0)
    percentage_scalers_2022 = round(percentage_scalers_2022, 0)
    percentage_scalers_2020 = round(percentage_scalers_2020, 0)
    percentage_scalers_2019 = round(percentage_scalers_2019, 0)
    percentage_scalers_2018 = round(percentage_scalers_2018, 0)


    selectpercentage_scaler_2021 = round(selectpercentage_scaler_2021, 0)
    selectpercentage_scaler_2022 = round(selectpercentage_scaler_2022, 0)
    selectpercentage_scaler_2020 = round(selectpercentage_scaler_2020, 0)
    selectpercentage_scaler_2019 = round(selectpercentage_scaler_2019, 0)
    selectpercentage_scaler_2018 = round(selectpercentage_scaler_2018, 0)
    
    
    fig, ax = plt.subplots()
    x = [2018, 2019, 2020, 2021, 2022]
    y = [percentage_scalers_2018, percentage_scalers_2019, percentage_scalers_2020, percentage_scalers_2021, percentage_scalers_2022]
    y2 = [selectpercentage_scaler_2018, selectpercentage_scaler_2019, selectpercentage_scaler_2020, selectpercentage_scaler_2021, selectpercentage_scaler_2022]
    ax.plot(x, y, label='All')
    ax.plot(x, y2, label='Selected')
    for i, txt in enumerate(y):
        ax.annotate(f'{txt}%', (x[i], y[i]), textcoords="offset points", xytext=(0,2), ha='center')
    for i, txt in enumerate(y2):
        ax.annotate(f'{txt}%', (x[i], y2[i]), textcoords="offset points", xytext=(0,2), ha='center')
    ax.set_xlabel('Year')
    ax.set_ylabel('Percentage of scaling companies')
    ax.set_title('Percentage of scaling companies over time')
    plt.legend()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    x = [2018, 2019, 2020, 2021, 2022]
    y2 = [selectnumber_scaler_2018, selectnumber_scaler_2019, selectnumber_scaler_2020, selectnumber_scaler_2021, selectnumber_scaler_2022]
    ax.plot(x, y2, label='Selected', color='orange')
    for i, txt in enumerate(y2):
        ax.annotate(f'{txt}', (x[i], y2[i]), textcoords="offset points", xytext=(0,2), ha='center')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of scaling companies')
    ax.set_title('Number of scaling companies over time')
    plt.legend()
    st.pyplot(fig)

    selecthighgrowth2021 = list(selectdata['HighGrowthFirm 2021'])
    selectpercentage_highgrowth_2021 = selecthighgrowth2021.count(1)/(selecthighgrowth2021.count(0)+selecthighgrowth2021.count(1))*100
    selectnumber_highgrowth_2021 = selecthighgrowth2021.count(1)

    selecthighgrowth2022 = list(selectdata['HighGrowthFirm 2022'])
    selectpercentage_highgrowth_2022 = selecthighgrowth2022.count(1)/(selecthighgrowth2022.count(0)+selecthighgrowth2022.count(1))*100
    selectnumber_highgrowth_2022 = selecthighgrowth2022.count(1)

    selecthighgrowth2020 = list(selectdata['HighGrowthFirm 2020'])
    selectpercentage_highgrowth_2020 = selecthighgrowth2020.count(1)/(selecthighgrowth2020.count(0)+selecthighgrowth2020.count(1))*100
    selectnumber_highgrowth_2020 = selecthighgrowth2020.count(1)

    selecthighgrowth2019 = list(selectdata['HighGrowthFirm 2019'])
    selectpercentage_highgrowth_2019 = selecthighgrowth2019.count(1)/(selecthighgrowth2019.count(0)+selecthighgrowth2019.count(1))*100
    selectnumber_highgrowth_2019 = selecthighgrowth2019.count(1)

    selecthighgrowth2018 = list(selectdata['HighGrowthFirm 2018'])
    selectpercentage_highgrowth_2018 = selecthighgrowth2018.count(1)/(selecthighgrowth2018.count(0)+selecthighgrowth2018.count(1))*100
    selectnumber_highgrowth_2018 = selecthighgrowth2018.count(1)

    percentage_highgrowth_2021 = round(percentage_highgrowth_2021, 0)
    percentage_highgrowth_2022 = round(percentage_highgrowth_2022, 0)
    percentage_highgrowth_2020 = round(percentage_highgrowth_2020, 0)
    percentage_highgrowth_2019 = round(percentage_highgrowth_2019, 0)
    percentage_highgrowth_2018 = round(percentage_highgrowth_2018, 0)
    
    selectpercentage_highgrowth_2021 = round(selectpercentage_highgrowth_2021, 0)
    selectpercentage_highgrowth_2022 = round(selectpercentage_highgrowth_2022, 0)
    selectpercentage_highgrowth_2020 = round(selectpercentage_highgrowth_2020, 0)
    selectpercentage_highgrowth_2019 = round(selectpercentage_highgrowth_2019, 0)
    selectpercentage_highgrowth_2018 = round(selectpercentage_highgrowth_2018, 0)
    

    fig, ax = plt.subplots()
    x = [2018, 2019, 2020, 2021, 2022]
    y = [percentage_highgrowth_2018, percentage_highgrowth_2019, percentage_highgrowth_2020, percentage_highgrowth_2021, percentage_highgrowth_2022]
    y2 = [selectpercentage_highgrowth_2018, selectpercentage_highgrowth_2019, selectpercentage_highgrowth_2020, selectpercentage_highgrowth_2021, selectpercentage_highgrowth_2022]
    ax.plot(x, y, label='All')
    ax.plot(x, y2, label='Selected')
    for i, txt in enumerate(y):
        ax.annotate(f'{txt}%', (x[i], y[i]), textcoords="offset points", xytext=(0,2), ha='center')
    for i, txt in enumerate(y2):
        ax.annotate(f'{txt}%', (x[i], y2[i]), textcoords="offset points", xytext=(0,2), ha='center')
    ax.set_xlabel('Year')
    ax.set_ylabel('Percentage of high growth companies')
    ax.set_title('Percentage of high growth companies over time')
    plt.legend()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    x = [2018, 2019, 2020, 2021, 2022]
    y2 = [selectnumber_highgrowth_2018, selectnumber_highgrowth_2019, selectnumber_highgrowth_2020, selectnumber_highgrowth_2021, selectnumber_highgrowth_2022]
    ax.plot(x, y2, label='Selected', color='orange')
    
    for i, txt in enumerate(y2):
        ax.annotate(f'{txt}', (x[i], y2[i]), textcoords="offset points", xytext=(0,2), ha='center')
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of high growth companies')
    ax.set_title('Number of high growth companies over time')
    plt.legend()
    st.pyplot(fig)

    selectconsistenthighgrowth2021 = list(selectdata['ConsistentHighGrowthFirm 2021'])
    selectpercentage_consistenthighgrowth_2021 = selectconsistenthighgrowth2021.count(1)/(selectconsistenthighgrowth2021.count(0)+selectconsistenthighgrowth2021.count(1))*100
    selectnumber_consistenthighgrowth_2021 = selectconsistenthighgrowth2021.count(1)

    selectconsistenthighgrowth2022 = list(selectdata['ConsistentHighGrowthFirm 2022'])
    selectpercentage_consistenthighgrowth_2022 = selectconsistenthighgrowth2022.count(1)/(selectconsistenthighgrowth2022.count(0)+selectconsistenthighgrowth2022.count(1))*100
    selectnumber_consistenthighgrowth_2022 = selectconsistenthighgrowth2022.count(1)

    selectconsistenthighgrowth2020 = list(selectdata['ConsistentHighGrowthFirm 2020'])
    selectpercentage_consistenthighgrowth_2020 = selectconsistenthighgrowth2020.count(1)/(selectconsistenthighgrowth2020.count(0)+selectconsistenthighgrowth2020.count(1))*100
    selectnumber_consistenthighgrowth_2020 = selectconsistenthighgrowth2020.count(1)

    selectconsistenthighgrowth2019 = list(selectdata['ConsistentHighGrowthFirm 2019'])
    selectpercentage_consistenthighgrowth_2019 = selectconsistenthighgrowth2019.count(1)/(selectconsistenthighgrowth2019.count(0)+selectconsistenthighgrowth2019.count(1))*100
    selectnumber_consistenthighgrowth_2019 = selectconsistenthighgrowth2019.count(1)

    selectconsistenthighgrowth2018 = list(selectdata['ConsistentHighGrowthFirm 2018'])
    selectpercentage_consistenthighgrowth_2018 = selectconsistenthighgrowth2018.count(1)/(selectconsistenthighgrowth2018.count(0)+selectconsistenthighgrowth2018.count(1))*100
    selectnumber_consistenthighgrowth_2018 = selectconsistenthighgrowth2018.count(1)

    percentage_consistenthighgrowth_2021 = round(percentage_consistenthighgrowth_2021, 2)
    percentage_consistenthighgrowth_2022 = round(percentage_consistenthighgrowth_2022, 2)
    percentage_consistenthighgrowth_2020 = round(percentage_consistenthighgrowth_2020, 2)
    percentage_consistenthighgrowth_2019 = round(percentage_consistenthighgrowth_2019, 2)
    percentage_consistenthighgrowth_2018 = round(percentage_consistenthighgrowth_2018, 2)
    

    selectpercentage_consistenthighgrowth_2021 = round(selectpercentage_consistenthighgrowth_2021, 2)
    selectpercentage_consistenthighgrowth_2022 = round(selectpercentage_consistenthighgrowth_2022, 2)
    selectpercentage_consistenthighgrowth_2020 = round(selectpercentage_consistenthighgrowth_2020, 2)
    selectpercentage_consistenthighgrowth_2019 = round(selectpercentage_consistenthighgrowth_2019, 2)
    selectpercentage_consistenthighgrowth_2018 = round(selectpercentage_consistenthighgrowth_2018, 2)
    
    fig, ax = plt.subplots()

    x = [2018, 2019, 2020, 2021, 2022]
    y = [percentage_consistenthighgrowth_2018, percentage_consistenthighgrowth_2019, percentage_consistenthighgrowth_2020, percentage_consistenthighgrowth_2021, percentage_consistenthighgrowth_2022]
    y2 = [selectpercentage_consistenthighgrowth_2018, selectpercentage_consistenthighgrowth_2019, selectpercentage_consistenthighgrowth_2020, selectpercentage_consistenthighgrowth_2021, selectpercentage_consistenthighgrowth_2022]
    ax.plot(x, y, label='All')
    ax.plot(x, y2, label='Selected')
    for i, txt in enumerate(y):
        ax.annotate(f'{txt}%', (x[i], y[i]), textcoords="offset points", xytext=(0,2), ha='center')
    for i, txt in enumerate(y2):
        ax.annotate(f'{txt}%', (x[i], y2[i]), textcoords="offset points", xytext=(0,2), ha='center')
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Percentage of consistent high growth companies')
    ax.set_title('Percentage of consistent high growth companies over time')
    plt.legend()
    st.pyplot(fig)

    fig, ax = plt.subplots()

    x = [2018, 2019, 2020, 2021, 2022]
    y2 = [selectnumber_consistenthighgrowth_2018, selectnumber_consistenthighgrowth_2019, selectnumber_consistenthighgrowth_2020, selectnumber_consistenthighgrowth_2021, selectnumber_consistenthighgrowth_2022]
    ax.plot(x, y2, label='Selected', color='orange')
    
    for i, txt in enumerate(y2):
        ax.annotate(f'{txt}', (x[i], y2[i]), textcoords="offset points", xytext=(0,2), ha='center')
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of consistent high growth companies')
    ax.set_title('Number of consistent high growth companies over time')
    plt.legend()
    st.pyplot(fig)
else:
    st.write('Please click the button to perform an operation')