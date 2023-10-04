import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def overview_page(data):
    st.header("Data Description")
    st.write(data)

def visualization_page(data):
    gender_math_mean = data.groupby('gender')['math score'].mean()

    st.subheader("Nilai Ujian Matematika")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    data['math score'].plot.hist(bins=10)
    st.pyplot()

    st.subheader("Gender Counts")
    gender_counts = data['gender'].value_counts().sort_index()
    st.bar_chart(gender_counts)

    st.subheader("Normalized Gender Counts")
    normalized_gender_counts = data['gender'].value_counts(normalize=True).sort_index()
    st.bar_chart(normalized_gender_counts)

    st.subheader("Box Plot of Math Scores by Gender")
    fig, ax = plt.subplots()
    data.boxplot(column=['math score'], by='gender', ax=ax)
    st.pyplot(fig)

def main():
    data = pd.read_csv("StudentsPerformance.csv", sep=",")
    st.title("Student Performance Analysis")
    selected_page = st.sidebar.selectbox("Select Page:", ["Overview", "Visualization"])

    if selected_page == "Overview":
        overview_page(data)
    elif selected_page == "Visualization":
        visualization_page(data)

if __name__ == '__main__':
    main()
