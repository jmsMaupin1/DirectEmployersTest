import feedparser

rss_url = "https://dejobs.org/jobs/feed/rss?q=nurse&location=Indianapolis%2C+IN&r=25"

def pull_job_links_from_feed(feed_url):
    feed = feedparser.parse(feed_url)

    if feed.status == 200:
        for entry in feed.entries:
            print(entry.link)

if __name__ == "__main__":
    pull_job_links_from_feed(rss_url)
