# Contents of ~/my_app/streamlit_app.py
import streamlit as st
from pages.Introduction import intro
from pages.Dataset import dataset
from pages.Analysis import analysis
from pages.Methods import methods
from pages.UI import ui

st.set_page_config('MDST Movie Recs', 'https://avatars.githubusercontent.com/u/15266139?s=200&v=4')

page_names_to_funcs = {
    "Introduction": intro,
    "Dataset": dataset,
    "Analysis": analysis,
    "Methods": methods,
    "UI": ui,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()