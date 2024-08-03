import subprocess
import os
import sys
import logging
sys.path.append("./")
subprocess.run("python -m venv ./env")
subprocess.run(".\env\Scripts\Activate.bat",shell=True)
subprocess.run("pip install ffmpeg")
subprocess.run("pip install -r requirements.txt")
subprocess.run("streamlit run app.py")
