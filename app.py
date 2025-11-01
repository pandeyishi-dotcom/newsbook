# app.py
import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Bluechip Fund News", layout="wide")

st.title("📰 Bluechip Fund News Tracker")
st.caption("Get the latest headlines about India’s top Bluechip Mutual Funds.")

# -------------------------------
# HELPER FUNCTION
# -------------------------------
def get_news(query, days):
    """Fetches Google News RSS results filtered by recency."""
    base_url = "https://news.google.com/rss/search"
    params = {"q": query, "hl": "en-IN", "gl": "IN", "ceid": "IN:en"}
    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        return []

    df = pd.read_xml(response.text)
    df["pubDate"] = pd.to_datetime(df["pubDate"], errors="coerce")

    cutoff = datetime.now() - timedelta(days=days)
    df = df[df["pubDate"] >= cutoff]
    df = df.sort_values("pubDate", ascending=False).reset_index(drop=True)
    return df[["title", "link", "pubDate"]]

# -------------------------------
# TIME RANGE SELECTOR
# -------------------------------
time_period = st.sidebar.radio(
    "Select News Period:",
    {
        "Last Week (7 days)": 7,
        "Last Month (30 days)": 30,
        "Last 3 Months (90 days)": 90,
        "Last 6 Months (180 days)": 180
    }
)

# -------------------------------
# BLUECHIP FUNDS LIST
# -------------------------------
funds = [
    "Axis Bluechip Fund",
    "ICICI Prudential Bluechip Fund",
    "HDFC Bluechip Fund",
    "Mirae Asset Large Cap Fund",
    "SBI Bluechip Fund",
    "Kotak Bluechip Fund"
]

# -------------------------------
# FETCH AND DISPLAY NEWS
# -------------------------------
for fund in funds:
    with st.expander(f"🟦 {fund}"):
        data = get_news(fund, time_period)
        if data.empty:
            st.info("No recent news found for this period.")
        else:
            for _, row in data.iterrows():
                st.markdown(f"**[{row['title']}]({row['link']})**")
                st.caption(f"🗓 Published on {row['pubDate'].strftime('%d %b %Y')}")
                st.markdown("---")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown(
    """
    ---
    🔍 Data Source: Google News RSS  
    ⚙️ Built with Streamlit | Developer: Ishu Pandey
    """
)
