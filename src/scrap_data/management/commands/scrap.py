import re
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.db import models
from scrap_data.models import Scrap
from django.core.management.base import BaseCommand
from datetime import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = "http://www.allagents.co.uk/rss/emoov/"
        try:
            redditFile = urlopen(url)
            redditcontent = redditFile.read()
            redditFile.close()

            content = redditcontent
            soup = BeautifulSoup(content)
            elements = soup.findAll('item')
            for element in elements:
                title = element.find('title').text
                description = element.find('description').text
                pubdate = datetime.strptime(element.find('pubdate').text, "%a, %d %b %Y %H:%M:%S %z")

                link = element.find('link').text
                guid = element.find('guid').text
                try:
                    Scrap.objects.get(guid=guid)
                    print(title , "is already exists!!!!")
                except Scrap.DoesNotExist:
                    record = Scrap(
                        title=title,
                        description=description,
                        pubdate=pubdate,
                        link=link,
                        guid=guid
                    )
                    record.save()
        except OSError:
            print("Please check your internet connection or try again later")
