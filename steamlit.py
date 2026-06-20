import streamlit as st
import sqlite3
import pandas as pd
from groq import Groq
import os

st.set_page_config(page_title="Scout AI", page_icon="⚽", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0a0a0a; }
    .stTextInput > div > div > input { background-color: #1a1a1a; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("⚽ Scout AI")
st.caption("Football Scouting Intelligence System — Top 5 Leagues · 2,852 Players")

client = Groq(api_key='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'
)

schema = """
Table: players
Columns: Player, Nation, Pos, Squad, Comp, Age, Min, Gls, Ast, xG, xAG, 
PrgC, PrgP, PrgR, Gls_90, Ast_90, xG_90, xAG_90, CrdY, CrdR, Player_Type
"""

def generate_sql(question):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": f"""You are a SQL expert.
            Given this database schema: {schema}
            Convert the user's football scouting question into a SQLite query.
            Return ONLY the SQL query, nothing else.
            Important:
            - Always SELECT *
            - Use Pos LIKE '%FW%' for positions
            - Always add Min > 500
            - Always LIMIT 10"""},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

def run_query(sql):
    conn = sqlite3.connect('scouts.db')
    result = pd.read_sql(sql, conn)
    conn.close()
    return result

question = st.text_input("Ask anything about players", placeholder="Find me a pressing winger under 23 with high progressive carries...")

col1, col2, col3 = st.columns(3)
with col1:
    league = st.selectbox("League", ["All", "Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1"])
with col2:
    max_age = st.number_input("Max age", min_value=16, max_value=40, value=35)
with col3:
    position = st.selectbox("Position", ["All", "Forward", "Midfielder", "Defender"])

if st.button("Find Players ⚽") and question:
    with st.spinner("Scouting..."):
        try:
            sql = generate_sql(question)
            st.code(sql, language="sql")
            result = run_query(sql)
            if result.empty:
                st.warning("No players found. Try a different search.")
            else:
                st.dataframe(result[['Player', 'Pos', 'Squad', 'Comp', 'Age', 'xG_90', 'PrgC', 'Player_Type']], use_container_width=True)
        except Exception as e:
            st.error(f"Error: {e}")