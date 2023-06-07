from Crawler import Crawler





if __name__ == '__main__':
    target_url = input("Enter the URL: ")
    # Create a new instance of the class
    crawler = Crawler(target_url)

    # Start the crawling process
    crawler.crawl()

    # Print the results
    crawler.print_results()

    # Save the results to a file
    crawler.save_results()

    # Print the time taken to crawl
    crawler.print_time_taken()

    # Print the number of links found
    crawler.print_num_links()



# Path: main.py





