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
    self.demo_images_dict = {0: {'src': 'https://cvws.icloud-content.com/S/AbjDnPT4gkojdj-EESS_38NzCtph/IMG_0008.JPG?o=AtTsKIACA676F92HIvwuaIrdCQP1VHBHAVzBs_jREhJN&v=1&z=https%3A%2F%2Fp50-content.icloud.com%3A443&x=1&a=CAog7Jw2FcGJ96hbUrDIRUm5t_AKApC3HaH5uXxEFFTg0LESZRDWwpHPkS8Y1tmk1JEvIgEAUgRzCtphaiX_h8AOBGRvWNOcCBXzmk84awu8JNT0p_KQtYd81fSojO9_VBT6ciVLsCZvbe5Pe1f2w9bshKLWlPCIwAc4_gz0KdDL3bbwOdHTdu8x&e=1619647868&r=7f0f76d8-ac99-4646-8d5b-f07c7d816c7f-12&s=7u28rh6ZHDsrjOuOg5OK1cjIjmk', 'text': 'recess time...'}, 1: {'src': 'https://cvws.icloud-content.com/S/Ab2Rgwdj3BOyQCD6_z3tgJnXCW9f/IMG_0007.JPG?o=AglTg-q9ipEv7OgfwBPozzhdRvkhWqGTNsM1iwU7I1Gf&v=1&z=https%3A%2F%2Fp50-content.icloud.com%3A443&x=1&a=CAogSSZE1phk572edS-DdhZmLzJ6rQdccYwmdVUWtTbzpgcSZRDTm5LPkS8Y07Kl1JEvIgEAUgTXCW9faiUk6NLCWSIa0V67UMUZhtGukm1uNvqz6ZnuonrHokrQ39Id5MF1ciWj5jybFBDDXNUOIb6pbiYX131OcLFSsLmwA1kz-vyFZIOCSUHB&e=1619647879&r=3d22c009-eb9c-4e88-b767-abc17ca0a53d-13&s=h-HygGu61nQsyHoHnyl6pIqY2KU', 'text': 'countin grooves...'}, 2: {'src': 'https://cvws.icloud-content.com/S/AZ2UbOfx7JNXsokq4V1KmmypyA1y/IMG_0005.JPG?o=AofSUiq1O4WHb4p8lU2_h6IjxPbTjVORR82X1-HybANJ&v=1&z=https%3A%2F%2Fp50-content.icloud.com%3A443&x=1&a=CAogfvhwH8x72HLi4LOLWvVrz8jGRqm0VB7dfZn1jsmkh6YSZRDM6pLPkS8YzIGm1JEvIgEAUgSpyA1yaiU1TKOypx91QppNZtahBMm0uhR2o_8vXqW_uXV2MtIJ4qT1WjmFciUmQ3bHrccU_F6XLt9fLCiS2JWoAI-UcQkhKiDWUXFBcSPowASp&e=1619647889&r=4316c4d9-498a-46b7-9c88-10b0e2ef6620-9&s=e8FGPFz-oid2J_81KhdzQtrj1LE', 'text': 'finally ready for detailing...'}}
    
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


  def generate_collages(self):
    # Scrapes iCloud album with studio images ✅
    # self.__scrape_iphoto_album(self.iphoto_url_images, "./files/output_images")
    
    # Generates 25 new collages in local directory
    # for i in range(25):
    self.__generate_collage()

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

  def __scrape_iphoto_album(self, iphoto_url):
    print(f"Running __scrape_iphoto_album()...")
    self.driver.get(iphoto_url)
    sleep(3)
    print(f"Selenium successfully reached {self.driver.title}...")
    images = self.driver.find_elements_by_class_name("x-stream-photo-group-blocks-container-view")
    print(f"Running get_image() for {len(images)} found images...")

    for i in range(len(images)):
      images[i].click()
      print(f"Retreiving image {i}...")
      sleep(3)
      current_image = self.driver.find_element_by_tag_name("img")
      current_image_source = current_image.get_attribute("src")
      current_image_text_element = self.driver.find_element_by_class_name("main")
      current_image_text = current_image_text_element.get_attribute("innerText")
      print(f"Processing image associated with '{current_image_text}'...")
      self.images_dict[i] = { "src": current_image_source, "text": current_image_text }
      urllib.request.urlretrieve(current_image_source, f"input_images/{current_image_text}.png")
      self.driver.back()
      sleep(3)
      images = self.driver.find_elements_by_class_name("x-stream-photo-group-blocks-container-view")
      print(self.images_dict)



  def __generate_collage(self):
    os.system("bash collage_script.sh")


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
