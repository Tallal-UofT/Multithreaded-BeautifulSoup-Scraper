# What is it?
A Multithreaded BeautifulSoup Scraper with appropriate headers. 

# What does it do?
BeautifulSoup in its original form sends requests one at a time (i.e. Single Processor use). Unlike Scrapy it is not built for sending multiple requests at a time. The following code allows us to run a multi-threaded BeautifulSoup Scraper (i.e. sending multiple requests at a time). Thereby speeding up any scraping process.

The headers ensure that most websites will not flag the scrapper and block the IP address. Additional protection in the form of random time delays are also put in place.

In order to combat sights that Connectivity Issues, the Scraper also uses multiple tries to access a URL.
