import data_viz, hypotest
import streamlit as st

PAGES = {'Data Visualization' : data_viz,
         'Hypothesis testing' : hypotest
         }

selected = st.sidebar.selectbox('Pages: ', list(PAGES.keys()))

page = PAGES[selected]

page.app()

