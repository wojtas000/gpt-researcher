from trafilatura import fetch_url, extract
from trafilatura.settings import use_config
from ..beautiful_soup.beautiful_soup import BeautifulSoupScraper

class DocsAiScraper:
    """
    DocsAiScraper class to extract the content from the links
    """

    def __init__(self, link, session=None, snippet=""):
        """
        Initialize the DocsAiScraper class.
        Args:
            link:
            session:
        """
        self.link = link
        self.session = session
        self.snippet = snippet
        self.config = use_config()
        self.backup_scraper = BeautifulSoupScraper(self.link, self.session)

    def scrape(self):
        """
        Extracts the content from the link using trafilatura library
        """
        response = fetch_url(self.link)
        if response is not None:
            return extract(response, config=self.config, no_fallback=True)
        else:
            return self.packup_scraper.scrape()