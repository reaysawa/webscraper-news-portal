# Introduction

This is an application that crawls news websites and displays the head titles in a front page.

The things to look out for are:

#### Shared ORM
The persistence layer for storing crawler results is the same as the one used in the main app (i.e. the Django ORM for PortalDjangoApp).
#### You can emulate a live crawling target by using scripts...
Doing the following:
  - Create a local copy, with assets included, of a single website's page, using `wget`. It will converts links to the filesystem's structure, thus virtually "routing" even foreign assets to the same server.
  - Run the mirrored local copy with `python -m http.server`, a built-in module, to serve the crawl target in the local network.

**TL;DR** you can crawl as much as you want in a development environment.
#### The app
A small app built with Django templates for filtering news by it's domain.

# How to run
## 1. Install the dependencies
`pip install -r requirements.txt`
## 2. Create the database
```sh
cd PortalDjangoApp && ./manage.py migrate
```
It will create a db.sqlite3 file in the same folder.
## 3. Running...
### 3.1 Locally
- A [Tecmundo](https://www.tecmundo.com.br) dummy copy is already available at the fixtures folder.
```sh
cd fixtures/tecmundo && python -m http.server
```
- In another terminal - notice the switch for development
```sh
cd ScraperScrapyApp && scrapy crawl TecMundoSpider -a env=DEV
```
### 3.2 Against the real Tecmundo website
```sh
cd ScraperScrappyApp && scrapy crawl TecMundoSpider
```
**Note:** After crawling, you can shut down both the server and the crawler.
## 4. Checking out the results
```sh
cd PortalDjangoApp && ./manage.py runserver
```

# Additional setup
## Crawling
### Make a local copy for crawling locally
`scripts/single_page_mirror [URL] [name_of_folder]`
### Change into the crawled copy and run the server
`cd fixtures/[name_of_folder] && python -m http.server`

