import streamlit as st
from home import main as home_page
from main_functionality import main as functionality_page
from about import main as about_page
from data_visual import main as data_visual


def main():
    # Display profile picture in circular view
    st.sidebar.image("shawn.png", use_column_width=True, output_format='JPEG', width=5, caption="ST Media")
    
    # Centered title
    st.markdown("<h1 style='text-align: center;'>🎬 Media control with Hand Gestures</h1>", unsafe_allow_html=True)
    
    # Navigation bar
    st.sidebar.title("Navigation")
    pages = ["Home", "Main Functionality", "Data Visualization","About"]
    selected_page = st.sidebar.selectbox("Select Page", pages)

    if selected_page == "Home":
        home_page()
    elif selected_page == "Main Functionality":
        functionality_page()
    elif selected_page == "Data Visualization":
        data_visual()
    elif selected_page == "About":
        about_page()

if __name__ == "__main__":
    main()
