class Codec:
    def __init__(self):
        self.url_to_tiny = {}
        self.tiny_to_url = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl not in self.url_to_tiny:
            shortUrl = self.base + str(len(self.url_to_tiny) + 1)
            self.url_to_tiny[longUrl] = shortUrl
            self.tiny_to_url[shortUrl] = longUrl

        return self.url_to_tiny[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.tiny_to_url[shortUrl]


url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
print(codec.decode(codec.encode(url)))