import streamlit as st
import feedparser
import urllib.parse

def get_news_rss():
    feed = feedparser.parse("https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en")

    st.subheader("📰 Top 5 News Headlines:")
    for i, entry in enumerate(feed.entries[:5], start=1):
        title = entry.title
        link = entry.link

        # Clean up the Google redirect link
        if "news.google.com" in link and "url=" in link:
            parsed_link = urllib.parse.parse_qs(urllib.parse.urlparse(link).query)
            link = parsed_link.get("url", [link])[0]

        # Display each headline as a clickable link
        st.markdown(f"**{i}. {title}**  \n👉 [Read more]({link})", unsafe_allow_html=True)
