from bs4 import BeautifulSoup
import requests
import os
from multiprocessing import Pool
# Replace with the URL that has the directory listing for the ebooks
base_url= "http://www.digitaldreamart.com/storage/books/"
# Replace with the path where you would like to store the downloaded ebooks
directory = "/Users/prateek/Ebooks/"

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