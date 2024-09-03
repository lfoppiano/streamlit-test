import os.path

from streamlit_pdf_viewer import pdf_viewer

import streamlit as st

## Issue with Chrome

from glob import glob

if 'directory' not in st.session_state:
    st.session_state['directory'] = None


st.set_page_config(
    page_title="Streamlit test env",
    layout="wide",
    page_icon="",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/lfoppiano/streamlit-test',
        'Report a bug': 'https://github.com/lfoppiano/streamlit-test',
        'About': "Streamlit test"
    }
)


st.session_state.directory = st.text_input(
    help="Enter a directory with PDF documents",
    label="Directory with PDF documents"
)

if st.session_state.directory:
    if not (os.path.exists(st.session_state.directory)
            or os.path.isdir(st.session_state.directory)):
        st.error("The selected paths is not a directory or does not exists")
        st.stop()
    else:
        paths = glob(st.session_state.directory + '/*.pdf')
        for id, (tab, path) in enumerate(zip(st.tabs(paths),paths)):
            with tab:
                with st.container(height=600):
                    if id == 0:
                        pdf_viewer(path, width=500, render_text=True, key=id)
                    else:
                        pdf_viewer(path, width=1000, render_text=True, key=id)