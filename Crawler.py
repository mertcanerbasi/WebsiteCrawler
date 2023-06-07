from bs4 import BeautifulSoup
import requests
import time

class Crawler:

    def __init__(self, target_url):
        self.target_url = target_url
        self.response = requests.get("https://"+self.target_url).text
        self.st = time.time()
        self.et = time.time()
        self.urlLinks = []

    def crawl(self):
        # Crawl the target URL
        soup = BeautifulSoup(self.response, 'html.parser')
        for link in soup.find_all('a', href=lambda href: href is not None and href.startswith('https')):
            self.urlLinks.append(link['href'])
        self.et = time.time()

    def print_results(self):
        print(self.urlLinks)


    def save_results(self):
        with open("links.txt", "w") as f:
            for link in self.urlLinks:
                f.write(link+"\n")


    def print_time_taken(self):
        print("Done in {} seconds".format(self.et-self.st)  )

    def print_num_links(self):
        print("Found {} links".format(len(self.urlLinks)))
