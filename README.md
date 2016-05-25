# Book-Downloader (Python)

I came across multiple directory listing websites which host a lot of ebooks which I wanted to download personally. Hence I created a short Python script that uses BeautifulSoup to parse the HTML contents of such directory listing pages and goes through the list of books to download each of them. It uses the Requests library for the download process which happens using a thread pool thus allowing simultaneous downloads. There is no progress bar at the moment but it can be added later.
