# app.py
import streamlit as st
import feedparser
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Bluechip Fund News", layout="wide")

st.title("📰 Bluechip Fund News Tracker")
st.caption("Get the latest headlines about India’s top Bluechip Mutual Funds.")

def get_news(query, days):
    """Fetch Google News RSS for the query and filter by recent days."""
    base_url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
    parsed = feedparser.parse(base_url)

    if parsed.bozo and not parsed.entries:
        return pd.DataFrame(columns=["title", "link", "pubDate"])

    cutoff = datetime.utcnow() - timedelta(days=days)
    rows = []

    for entry in parsed.entries:
        title = entry.get("title", "No title")
        link = entry.get("link", "")
        published = entry.get("published_parsed")
        if published:
            pub_date = datetime(*published[:6])
            if pub_date >= cutoff:
                rows.append({"title": title, "link": link, "pubDate": pub_date})

    return pd.DataFrame(rows)

periods = {
    "Last Week (7 days)": 7,
    "Last Month (30 days)": 30,
    "Last 3 Months (90 days)": 90,
    "Last 6 Months (180 days)": 180
}

time_label = st.sidebar.radio("Select News Period:", list(periods.keys()))
time_days = periods[time_label]

funds = [
    "Axis Bluechip Fund",
    "ICICI Prudential Bluechip Fund",
    "HDFC Bluechip Fund",
    "Mirae Asset Large Cap Fund",
    "SBI Bluechip Fund",
    "Kotak Bluechip Fund"
]

selected_funds = st.sidebar.multiselect("Choose funds:", funds, default=funds[:3])

for fund in selected_funds:
    st.subheader(f"🔷 {fund}")
    df = get_news(fund, time_days)
    if df.empty:
        st.info("No recent news found.")
    else:
        for _, row in df.iterrows():
            st.markdown(f"**[{row['title']}]({row['link']})**")
            st.caption(f"🗓 {row['pubDate'].strftime('%d %b %Y %H:%M UTC')}")
            st.markdown("---")

st.markdown("---")
st.caption("🔍 Source: Google News RSS | ⚙️ Built with Streamlit by Ishu Pandey")
.
Traceback:
File "/mount/src/newsbook/app.py", line 65, in <module>
    data = get_news(fund, time_period)
File "/mount/src/newsbook/app.py", line 28, in get_news
    df["pubDate"] = pd.to_datetime(df["pubDate"], errors="coerce")
                                   ~~^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py", line 4113, in __getitem__
    indexer = self.columns.get_loc(key)
File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.py", line 3819, in get_loc
    raise KeyError(key) from err
