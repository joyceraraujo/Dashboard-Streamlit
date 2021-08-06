#!/bin/bash

yum update -y
yum install git -y
yum install python37 python37-virtualenv python37-pip -y

pip install --upgrade pip
cd /home/ec2-user
python3 -m venv /home/ec2-user/venv
source /home/ec2-user/venv/bin/activate
            
pip3 install pandas 
pip3 install streamlit 
pip3 install plotly.express


git clone https://github.com/joyceraraujo/Dashboard-Streamlit.git

cd /home/ec2-user/Dashboard-Streamlit
streamlit run main.py
# streamlit run main.py --server.port 8501 --server.enableCORS False
