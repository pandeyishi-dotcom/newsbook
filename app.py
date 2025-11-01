This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
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
