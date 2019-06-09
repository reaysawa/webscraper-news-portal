# -*- coding: utf-8 -*-

BOT_NAME = "ScraperScrapyApp"
LOG_LEVEL = "ERROR"

SPIDER_MODULES = ["ScraperScrapyApp.spiders"]
NEWSPIDER_MODULE = "ScraperScrapyApp.spiders"
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {"ScraperScrapyApp.pipelines.NewsHeadingPipeline": 1}
