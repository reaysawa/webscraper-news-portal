# Introduction

This is an application that crawls news websites and displays the main news in a front page.

The things to look out for are:

#### Shared ORM
The Django ORM is used both for the app and the crawlers. In the latter, it achieves this by [faking](https://github.com/resolritter/webscraper-news-portal/blob/d5baff39134a79549f23a500c6e44118698c8a83/ScraperScrapyApp/pipelines/django_setup.py#L10) the launch of the main app, so that the Django's general infrastructure becomes fully ready to persist data, as if it were running the actual app.
#### You can emulate a live crawling target by using scripts
  - The bash script will create a local copy, assets included, of a single website's page using `wget`. Links are automatically converted to the filesystem's structure, thus being able to serve even foreign assets as if it were the actual server making network requests.
  - The local mirror can be served `python -m http.server`, a built-in module. That enables you to practice and do dry scraping runs as much as you want in a development environment.
#### The app
A small app built with Django templates for filtering news by it's domain.

# Run the server

This repository ships with the website's and a sample database pre-populated already, so it's not needed to crawl upfront.

## 1. Install the dependencies
`pip install -r requirements.txt`
## 2. Run the server
```sh
cd PortalDjangoApp && ./manage.py runserver
```

# How to crawl and refresh by yourself
## 1. Install the dependencies
`pip install -r requirements.txt`
## 2. Create the database
```sh
cd PortalDjangoApp && ./manage.py migrate
```
It will create a db.sqlite3 file in the same folder.
## 3. Running...
### 3.1 Locally
- A [TecMundo](https://www.tecmundo.com.br) dummy copy is already available at the fixtures folder.
```sh
cd fixtures/tecmundo && python -m http.server
```
- In another terminal :exclamation::exclamation: notice the switch for development
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
`scripts/single_page_mirror.sh [URL] [name_of_folder]`
### Change into the crawled copy and run the server
`cd fixtures/[name_of_folder] && python -m http.server`

