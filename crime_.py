import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import numpy as np
#import geopandas as gpd
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
df=pd.read_csv(r"D:\youtube project\crime2.csv")
def data():
    df=pd.read_csv(r"D:\youtube project\crime2.csv")
    return df

def home():
    st.title("CRIME ANALAYSIS")
    st.header("MAIN OBJECTIVES OF THIS ANALYSIS")
    st.subheader("...")
    icon=Image.open(r"C:\Users\navit\OneDrive\Pictures\IMAGES\coper.png")
    st.image(icon,use_column_width=True)

def crime_type(df):
    st.title("CRIME ANALAYSIS BY PRIMARY TYPE")
    primary_type_counts = df['Primary Type'].value_counts().reset_index()
    primary_type_counts.columns = ['Primary Type', 'Count']

    # Plotting
    plt.figure(figsize=(12, 6))
    sns.barplot(data=primary_type_counts, x='Primary Type', y='Count')
    plt.title('Crime Counts by Primary Type')
    plt.xlabel('Primary Type')
    plt.ylabel('Count')
    plt.xticks(rotation=90)
    st.pyplot(plt.gcf(), clear_figure=True)
    
   
    crime_counts_years = df.groupby('Primary Type').size().reset_index(name='count')
    # Plotting
    plt.figure(figsize=(12, 6))
    sns.barplot(data=crime_counts_years, x='Primary Type', y='count')
    plt.title('Crime Count of each year')
    plt.xlabel('Primary Type')
    plt.ylabel('year')
    plt.xticks(rotation=90)
    st.pyplot(plt.gcf(), clear_figure=True)
    
    
def loca(df):
    st.title("CRIME ANALAYSIS BY LOCATION DESCRIPTION")
    location_description_counts = df['Location Description'].value_counts().reset_index()
    location_description_counts.columns = ['Location Description', 'Count']

    # Slice the DataFrame to include only the top 20 entries
    top_location_descriptions = location_description_counts.head(20)

    # Plotting
    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_location_descriptions, x='Location Description', y='Count')
    plt.title('Crime Counts by Location Description (Top 20)')
    plt.xlabel('Location Description')
    plt.ylabel('Count')
    plt.xticks(rotation=90)
    st.pyplot(plt.gcf(), clear_figure=True)
    
    st.title("ANALYSIS LOCATION DESCRIPTION VS BEAT")
    plt.figure(figsize=(16,8))
    sns.barplot(data=df, x="Location Description", y="Beat")
    plt.title('Comparison by Beat')
    plt.xticks(fontsize=4)
    plt.xticks(rotation=90)
    st.pyplot(plt.gcf(), clear_figure=True)
    
    st.title("ANALYSIS LOCATION DESCRIPTION VS CUMMUNITY AREA")
    plt.figure(figsize=(16,8))
    sns.barplot(data=df, x="Location Description", y="Community Area")
    plt.title('Comparison by Beat')
    plt.xticks(fontsize=4)
    plt.xticks(rotation=90)
    st.pyplot(plt.gcf(), clear_figure=True)
def geo(df):
    st.title("NUMBER OF CRIMES OF EACH DISTRICT")
    # Group by district and count crimes
    district_crime_counts = df.groupby('District').size().reset_index(name='Crime_Count')

    # Group by ward and count crimes
    ward_crime_counts = df.groupby('Ward').size().reset_index(name='Crime_Count')

    # Plot crime counts by district
    plt.figure(figsize=(12, 6))
    sns.barplot(x='District', y='Crime_Count', data=district_crime_counts)
    plt.title('Crime Counts by District')
    plt.xlabel('District')
    plt.ylabel('Number of Crimes')
    plt.xticks(rotation=90)
    st.pyplot(plt.gcf(), clear_figure=True)
    
    st.title("NUMBER OF CRIMES OF WARD")
    # Plot crime counts by ward
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Ward', y='Crime_Count', data=ward_crime_counts)
    plt.title('Crime Counts by Ward')
    plt.xlabel('Ward')
    plt.ylabel('Number of Crimes')
    plt.xticks(rotation=90)
    st.pyplot(plt.gcf(), clear_figure=True)
    
    df['DateTime'] = pd.to_datetime(df['Date'], format='%Y%m%d %I', errors='coerce').dt.date
    #df['DateTime'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %I')

    # Extract year, month, day, and hour from the 'DateTime' column
    df['year'] = df['DateTime'].dt.year
    df['month'] = df['DateTime'].dt.month
    df['day'] = df['DateTime'].dt.day
    df['hour'] = df['DateTime'].dt.hour

    # For monthly analysis
    df['year_month'] = df['DateTime'].dt.to_period('M')

    # For daily analysis
    df['date'] = df['DateTime'].dt.to_period('D')

    # Plot the number of crimes per year
    plt.figure(figsize=(12, 6))
    yearly_crimes = df.groupby('year').size()
    yearly_crimes.plot(kind='bar')
    plt.title('Number of Crimes per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Crimes')
    st.pyplot(plt.gcf(), clear_figure=True)

    # Plot the number of crimes per month
    plt.figure(figsize=(12, 6))
    monthly_crimes = df.groupby('year_month').size()
    monthly_crimes.plot(kind='line')
    plt.title('Number of Crimes per Month')
    plt.xlabel('Month')
    plt.ylabel('Number of Crimes')
    plt.show()



def calculate_arrest_rates(df):
    # Overall arrest rate
    overall_arrest_rate = df['Arrest'].mean() * 100

    # Arrest rate by crime type
    arrest_rate_by_crime_type = df.groupby('Primary Type')['Arrest'].mean() * 100

    # Arrest rate by location
    arrest_rate_by_location = df.groupby('Location Description')['Arrest'].mean() * 100

    # Arrest rate by year
    arrest_rate_by_year = df.groupby('Year')['Arrest'].mean() * 100

    return overall_arrest_rate, arrest_rate_by_crime_type, arrest_rate_by_location, arrest_rate_by_year

# Step 2: Compare Domestic vs. Non-Domestic Crimes
def compare_domestic_non_domestic(df):
            # Domestic incidents
        domestic_incidents = df[df['Domestic'] == True]

            # Non-domestic incidents
        non_domestic_incidents = df[df['Domestic'] == False]

            # Characteristics and frequencies
        domestic_freq = domestic_incidents.shape[0]
        non_domestic_freq = non_domestic_incidents.shape[0]

            # Additional characteristics
        domestic_arrest_rate = domestic_incidents['Arrest'].mean() * 100
        non_domestic_arrest_rate = non_domestic_incidents['Arrest'].mean() * 100

        return domestic_freq, non_domestic_freq, domestic_arrest_rate, non_domestic_arrest_rate

        # Run the calculations
        overall_arrest_rate, arrest_rate_by_crime_type, arrest_rate_by_location, arrest_rate_by_year = calculate_arrest_rates(df)
        domestic_freq, non_domestic_freq, domestic_arrest_rate, non_domestic_arrest_rate = compare_domestic_non_domestic(df)

            # Print the results
        



    

def main():
    page=option_menu("select",["HOME","CRIME ANALYSIS","PREDICTION"],orientation="horizontal")
    if page=="HOME":
       
        st.write("Overall Arrest Rate: {:.2f}%")
        st.write("Overall Arrest Rate: {:.2f}%".format(overall_arrest_rate))
        st.write("Arrest Rate by Crime Type:\n", arrest_rate_by_crime_type)

        st.write("Arrest Rate by Location:\n", arrest_rate_by_location)
        st.write("Arrest Rate by Year:\n", arrest_rate_by_year)
        st.write("\nDomestic Incidents: ", domestic_freq)
        st.write("Non-Domestic Incidents: ", non_domestic_freq)
        st.write("Domestic Arrest Rate: {:.2f}%".format(domestic_arrest_rate))
        st.write("Non-Domestic Arrest Rate: {:.2f}%".format(non_domestic_arrest_rate))

    elif page=="CRIME ANALYSIS":
        #page1=st.sidebar.selectbox("SELECT", ["crime type analysis", "Temporal Analysis", "Location_specific analysis"])
        page1=option_menu("select the analysis type",["crime type analysis","Location_specific analysis","Temporal Analysis",],orientation='horizontal')
        if page1=="crime type analysis":
            crime_type(df)
        elif page1=="Location_specific analysis":
            loca(df)
        elif page1=="Temporal Analysis":
            geo(df)
            
    elif page=="PREDICTION":
        pass


if __name__ == "__main__":
    main()