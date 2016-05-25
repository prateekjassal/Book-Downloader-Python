from bs4 import BeautifulSoup
import requests
import os
import sys
from multiprocessing import Pool

class Book:

    def __init__(self, name, url):
        self.name = name
        self.url = url


def downloadBook(book):
    try:
        path = directory + book.name
        # Skip books that already exist
        if os.path.isfile(path) == True:
            # print 'Skipping '+book.name
            return
        print 'Downloading '+book.name
        r = requests.get(base_url + book.url)
        with open(path, 'wb') as b:
            b.write(r.content)
    except ChunkedEncodingError:
        return


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Error: The script needs 2 arguments - URL/link for the book listing, local path for saving the downloaded books"
        exit()
    script, base_url, directory = sys.argv
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text,"html.parser")
    list = soup.find('ul')
    list_objects = list.findAll('li')
    list_objects.pop(0)
    books = []
    for list_item in list_objects:
        item_url_object = list_item.find('a')
        book = Book(item_url_object.text.encode().strip(), item_url_object['href'].encode().strip())
        books.append(book)

    if not os.path.exists(directory):
        os.makedirs(directory)
    pool = Pool(8)
    for book in books:
        pool.map(downloadBook, books)