import feedparser
import asyncio
import aiohttp
from typing import List, Dict

class RSSFeedHandler:
    def __init__(self, feed_urls: List[str]):
        self.feed_urls = feed_urls
        self.feed_data: Dict[str, List[str]] = {url: [] for url in feed_urls}

    async def fetch_feed(self, url: str, session: aiohttp.ClientSession) -> None:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.text()
                    feed = feedparser.parse(content)
                    self.feed_data[url] = [entry.title for entry in feed.entries]
        except Exception as e:
            print(f"Error fetching feed from {url}: {e}")

    async def update_feeds(self) -> None:
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_feed(url, session) for url in self.feed_urls]
            await asyncio.gather(*tasks)

    def get_news_items(self) -> List[str]:
        all_items = []
        for items in self.feed_data.values():
            all_items.extend(items)
        return all_items

    async def run_updates(self, update_interval: int = 300) -> None:
        while True:
            await self.update_feeds()
            await asyncio.sleep(update_interval)  # Update every 5 minutes by default