# -*- coding: utf-8 -*-
from scrapy.http.response import Response
import scrapy


class UaMadeSpider(scrapy.Spider):
    name = 'uamade'
    start_urls = ['https://uamade.ua/uk/']

    def parse(self, response: Response):
        products = response.xpath("//div[contains(@class, 'ypi-grid-list__item_body')]")[:20]
        for product in products:
            yield {
                'description': product.xpath(".//a[@class='product-title']/@title").get(),
                'price': product.xpath(".//span[@class='ty-price-num']/text()").get(),
                'img': product.xpath(".//img[@class='ty-pict cm-image']/@src").get()
            }
