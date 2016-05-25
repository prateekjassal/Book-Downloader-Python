# Book-Downloader (Python)

I came across multiple directory listing websites which host a lot of ebooks(epubs in my case) which I wanted to download personally. Hence I created a short Python script that uses BeautifulSoup to parse the HTML contents of such directory listing pages and goes through the list of books to download each of them. It uses the Requests library for the download process which happens using a thread pool thus allowing simultaneous downloads. There is no progress bar at the moment but it can be added later.

Also, in case something goes wrong during the download i.e. for instance the connection breaks, you can run the script again and it would skip downloading the files that already exist and download only the remaining ones. 
However, it currently cannot detect if a file has been partially written. In this case it would simply skip this file. Such a file would need to be manually deleted in order to download it again.

Here are some of the listing sites I came across:

1. http://www.digitaldreamart.com/storage/books/
2. http://inzania.com/temp/kindle/books/
