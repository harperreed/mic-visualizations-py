import pygame
import asyncio
from ui.rss_feed_handler import RSSFeedHandler

class TopScroller:
    def __init__(self, width, height, rss_urls, speed=2):
        self.width = width
        self.height = height
        self.speed = speed
        self.font = pygame.font.Font(None, 36)
        
        self.rss_handler = RSSFeedHandler(rss_urls)
        self.news_items = []
        self.scroll_text = ""
        self.text_surface = None
        self.text_rect = None

        self.separator = "   •   "  # Separator between headlines

    async def start(self):
        asyncio.create_task(self.rss_handler.run_updates())
        asyncio.create_task(self.update_news_items())

    async def update_news_items(self):
        while True:
            new_items = self.rss_handler.get_news_items()
            if new_items:
                new_items = [item for item in new_items if item not in self.news_items]
                self.news_items.extend(new_items)
                
                new_text = self.separator.join(new_items)
                if self.scroll_text:
                    self.scroll_text += self.separator + new_text
                else:
                    self.scroll_text = new_text

                self.text_surface = self.font.render(self.scroll_text, True, (255, 255, 255))
                if not self.text_rect:
                    self.text_rect = self.text_surface.get_rect()
                    self.text_rect.y = 10
                    self.text_rect.x = self.width

            await asyncio.sleep(10)  # Check for new items every 10 seconds

    async def update(self, fft_data):
        if self.text_rect:
            self.text_rect.x -= self.speed
            
            if self.text_rect.right < 0:
                self.text_rect.x = self.width

            if len(fft_data) > 0:
                intensity = int(max(fft_data) * 255)
                color = (255, intensity, intensity)
                self.text_surface = self.font.render(self.scroll_text, True, color)

    def draw(self, screen):
        if self.text_surface and self.text_rect:
            screen.blit(self.text_surface, self.text_rect)
            if self.text_rect.right < self.width:
                screen.blit(self.text_surface, (self.text_rect.right, self.text_rect.y))