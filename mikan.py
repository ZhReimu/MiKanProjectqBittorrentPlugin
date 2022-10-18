# VERSION: 1.00
# AUTHORS: Mr.X (1725338233@qq.com)

# MIT License
#
# Copyright (c) 2022 Mr.X
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the right
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software i
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import feedparser

from helpers import download_file, retrieve_url
from novaprinter import prettyPrinter


# noinspection PyMethodMayBeStatic,SpellCheckingInspection,PyPep8Naming
class mikan(object):
    url = "https://mikanani.me/"
    name = "MikanProject"
    supported_categories = {"all": 0, "anime": 2}

    def download_torrent(self, info):
        """ Downloader """
        print(download_file(info))

    # DO NOT CHANGE the name and parameters of this function
    # This function will be the one called by nova2.py
    def search(self, what, cat='all'):
        """
        Here you can do what you want to get the result from the search engine website.
        Everytime you parse a result line, store it in a dictionary
        and call the prettyPrint(your_dict) function.

        `what` is a string with the search tokens, already escaped (e.g. "Ubuntu+Linux") `cat` is the name of a
        search category in ('all', 'movies', 'tv', 'music', 'games', 'anime', 'software', 'pictures', 'books')
        """
        html = retrieve_url(f'{self.url}RSS/Search?searchstr={what}')
        feed = feedparser.parse(html)
        for item in feed['entries']:
            link = [i for i in item.links if i.type == 'application/x-bittorrent'][0]
            prettyPrinter({
                "desc_link": item.link,
                "name": item.title.replace('\n', ''),
                "link": link.href,
                "size": link.length,
                "seeds": -1,
                "leech": -1,
                "engine_url": self.url
            })


if __name__ == '__main__':
    engine = mikan()
    engine.search('Akebi')
