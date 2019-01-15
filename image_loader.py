import numpy as np
import matplotlib.pyplot as plt
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

### Class to load in images to be used by neural net; load one day at a time to
### avoid having to store all the images
class ImageLoader:
    def __init__(self,url,start_date,stop_date,day_skip):
        self.url = url
        self.start_date = start_date
        self.stop_date = stop_date
        self.day_skip = day_skip
        pass

    def get_request(url = None):
        if url == None:
            url = self.url
        #return response
        pass
    
    def parse_html(date = None):
        if date == None:
            date = self.start_date
        ### Need <a link to images> on page date
        #return image link?
        pass

    def save_image(save_path = None)
        if save_path == None:
            save_path = self.save_path
        pass
