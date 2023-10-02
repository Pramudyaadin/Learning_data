import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.title('Data Visualization')

    st.header('Data Supermarket Sales')

    @st.cache
    def load_data():
        data = pd.read_csv('supermarket_sales - Sheet1.csv')
        return data
    
    df = load_data()

    st.write(df)

    st.subheader('Total supermarket sales')

    fig, ax = plt.subplots(figsize = [12,7])
    sns.histplot(df['Total'])
    st.pyplot(fig)

    st.subheader('Total product selling item per customer type')

    selected_product_customer = st.selectbox('Select customer type', options= (df['Product line'].unique()))

    fig1, ax1 = plt.subplots(figsize = [12,7])
    sns.histplot(df[df['Product line'] == selected_product_customer]['Customer type'])
    st.pyplot(fig1)

    with st.expander('Penjelasan grafik di atas'):
        st.write('Grafik di atas menampilkan berapa banyak item produk yang dibeli oleh masing-masing customer')

    st.subheader('Total customer type per city')

    selected_city_customer = st.selectbox('Select City', options= ('Yangon', 'Naypyitaw', 'Mandalay'))

    fig2, ax2 = plt.subplots(figsize = [12,7])
    sns.histplot(df[df['City'] == selected_city_customer]['Customer type'])
    st.pyplot(fig2)

    with st.expander('Penjelasan grafik di atas'):
        st.write('Grafik di atas menampilkan berapa banyak customer type pada setiap kota yang dipilih')
    
    st.subheader('Total Customer type per gender')

    selected_customer = st.selectbox('Select Customer type', options= ('Member', 'Normal'))

    fig3, ax3 = plt.subplots(figsize = [12,7])
    sns.histplot(df[df['Customer type'] == selected_customer]['Gender'])
    st.pyplot(fig3)

    with st.expander('Penjelasan grafik di atas'):
        st.write('Grafik di atas menampilkan jumlah gender pada customer type yang dipilih')

    st.subheader('Total product selling item per gender')

    selected_product_gender = st.selectbox('Select Product', options= (df['Product line'].unique()))

    fig4, ax4 = plt.subplots(figsize = [12,7])
    sns.histplot(df[df['Product line'] == selected_product_gender]['Gender'])
    st.pyplot(fig4)

    with st.expander('Penjelasan grafik di atas'):
        st.write('Grafik di atas menampilkan jumlah product item yang dibeli oleh gender yang dipilih')



    

    