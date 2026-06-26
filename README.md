Scout AI — Football Scouting Intelligence System
Live Demo: https://footballscoutingaiassistant.streamlit.app | GitHub: github.com/palakpb/football_scouting_ai_assistant

Overview
Scout AI is an end-to-end multi-agent football scouting system that lets scouts query a database of 2,852 players across the top 5 European leagues using plain English. Instead of manually filtering spreadsheets, a scout can type "Find me a pressing winger under 23 in the Bundesliga" and get ranked results instantly.

Features

Natural language to SQL conversion using Groq API (Llama 3.1)
2,852 player database across Premier League, La Liga, Bundesliga, Serie A, Ligue 1
K-Means clustering to classify players into tactical archetypes (Goal Poacher, Ball Carrier, Deep Playmaker, Progressive Passer, Box to Box, Assist King)
Filter by league, age, and position
Deployed on Streamlit Cloud — accessible from any browser


Tech Stack
LayerToolsDataPython, Pandas, SQLiteMLScikit-learn (K-Means)AIGroq API, Llama 3.1UIStreamlitDeploymentStreamlit Cloud

How It Works
Scout types a question in plain English
        ↓
Groq API (Llama 3.1) converts it to SQL
        ↓
SQLite database is queried
        ↓
Results ranked and returned with player archetypes

Project Structure
football_scouting_ai_assistant/
├── steamlit.py        ← Main Streamlit app
├── scouts.db          ← SQLite player database
├── requirements.txt   ← Dependencies
└── README.md

Setup Locally
bashgit clone https://github.com/palakpb/football_scouting_ai_assistant
cd football_scouting_ai_assistant
pip install -r requirements.txt
streamlit run steamlit.py
Add your Groq API key in .streamlit/secrets.toml:
tomlGROQ_API_KEY = "your_key_here"

Data Source
Player stats sourced from FBref top 5 leagues 2023-24 season via Kaggle.

Author
Palak Bhaiya — B.Tech ECE, Manipal University Jaipur
