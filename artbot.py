# Desired Experience
#   Start a new artbot
#   Give it "generate_collages" command 
#     Scrapes iCloud album with studio images
#     Generates 25 new collages in local directory
#     Maybe deletes 25 old collages first and keeps count at 100 (?)
#     Updates static html & markdown files for github pages page
#     Commits to git history and pushes to github
#   Give it single "instagram_session" command
#     Scrapes iCloud album with selected collages
#     Checks against static memory JSON file or github history to see whats new
#     Checks static memory JSON file for pending posts queue
#     Checks static memory JSON file for desired post frequency
#     Checks static memory JSON file for optimal hashtags
#     Determines next optimal post datetime
#     Initiates background process to make post at that time
#     Updates static memory JSON file
#     Commits to git history and pushes to github
from selenium import webdriver
from datetime import date
from time import sleep
import urllib.request
import json
import sys
import os

class ArtBot:
  def __init__(self):
    # load config settings
    self.settings = json.load(open('./config.json', 'r'))
    self.is_scraper_on = self.settings['scraper']['is_on']
    self.iphoto_url_images = self.settings['scraper']['iphoto_url_images']

    self.images_dict = {}
    
    # selenium driver
    self.driver = None
    if self.is_scraper_on: 
      self.options = webdriver.ChromeOptions()
      self.options_arguments = (f'user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:86.0) Gecko/20100101 Firefox/86.0"', "--window-size=1920,1080", '--ignore-certificate-errors', '--allow-running-insecure-content', "--disable-extensions", "--proxy-server='direct://'", "--proxy-bypass-list=*", "--start-maximized", '--disable-gpu', '--disable-dev-shm-usage', '--no-sandbox', '--disable-dev-shm-usage')
      for argument in self.options_arguments:
        self.options.add_argument(argument)
      self.options.headless = True
      self.driver = None
      self.driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=self.options)
    
    # instapy

    # test code
    print(self.is_scraper_on)
    pass

  def generate_collages(self):
    # Scrapes iCloud album with studio images
    self.__scrape_iphoto_album(self.iphoto_url_images, "./files/output_images")
    # Generates 25 new collages in local directory
    # Maybe deletes 25 old collages first and keeps count at 100 (?)
    # Updates static html & markdown files for github pages page
    # Commits to git history and pushes to github
    pass

  def instagram_session(self):
    # Scrapes iCloud album with selected collages
    # Checks against static memory JSON file or github history to see whats new
    # Checks static memory JSON file for pending posts queue
    # Checks static memory JSON file for desired post frequency
    # Checks static memory JSON file for optimal hashtags
    # Determines next optimal post datetime
    # Initiates background process to make post at that time
    # Updates static memory JSON file
    # Commits to git history and pushes to github
    pass

  def __scrape_iphoto_album(self, iphoto_url, output_folder):
    # self.driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=self.options)
    print(f"Running __scrape_iphoto_album()...")
    self.driver.get(iphoto_url)
    sleep(3)
    print(self.driver.title)

  def __generate_collage(self, source_folder, output_folder):
    pass

  def __instagram_post(self, username, password, source_folder):
    pass

  def __instagram_friends_interaction_session(self, username, password, friends_array, comments_array, like_count, comment_count, session_duration):
    # starts headless instagram session running in background
    # focuses on liking and commenting random recent posts by friends
    # might manually take friends list
    # might access friends list from instagram
    pass

  def __instagram_new_friends_session(self, username, password, hashtag_array, comments_array, like_count, comment_count, friend_request_count, session_duration):
    # likes and comments on posts associated with certain hashtags 
    # likes and comments on posts by friends of friends (if possible) 
    pass

  def __schedule_post(self, text, image_path, desired_datetime):
    # starts daemon or time-triggered event for next post
    pass

a = ArtBot()
a.generate_collages()
