import streamlit as st
import subprocess

def main():
    st.title("AI Virtual Mouse")

    if st.button("Start Camera"):
        start_opencv_code()

def start_opencv_code():
    # Start your existing OpenCV code as a subprocess
    subprocess.Popen(["python", "mouse.py"])


if __name__ == "__main__":
    main()
