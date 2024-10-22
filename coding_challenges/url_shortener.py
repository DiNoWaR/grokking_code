import base64
import threading

class UrlShortener:
    def __init__(self):
        self.storage = dict()
        self.lock = threading.RLock()

    def shorten(self, url) -> str:
        if not url:
            return ''
        else:
            return base64.b64encode(url.encode()).decode('utf-8')

    def store(self, url, short_url):
        if not url or not short_url:
            raise ValueError("Both 'url' and 'short_url' must be non-empty strings.")

        with self.lock:
            if short_url not in self.storage:
                self.storage[short_url] = url
                return
            else:
                return

    def get_url(self, short_url) -> str:
        if not short_url:
            return ''
        with self.lock:
            if short_url in self.storage:
                return self.storage[short_url]
            else:
                return ''