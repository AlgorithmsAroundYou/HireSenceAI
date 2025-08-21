
import webview
import threading
import subprocess

def run_streamlit_app():
    subprocess.Popen(["streamlit", "run", "Home.py"])

if __name__ == "__main__":
    # Start the Streamlit app in a separate thread
    threading.Thread(target=run_streamlit_app).start()

    # Create a webview window to display the Streamlit app
    webview.create_window("Agiliad AI Apps", "http://localhost:8501", with_browser=True, width=1200, height=800)
    webview.start() 