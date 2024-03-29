from random import random
import json
import os

class BotInfo:

  instance = None

  def __new__(cls):
    if cls.instance is None:
      cls.instance = super().__new__(cls)
      cls.instance.execution_id = int(random()*10**10)
    return cls.instance

  def __init__(self, bot_info_path = None):

    self.root_path = '\\'.join(__file__.split('\\')[:-3])
    self.bot_info_path =  f'{self.root_path}\\bot_info.json'

    if bot_info_path:
      self.bot_info_path = bot_info_path
      
    self.get_info()
  
  def get_info(self):
    f = open(self.bot_info_path)
    data = json.load(f)

    self.data = data
    self.name = data['name']
    self.columns_analytical = data['columns_analytical']
    self.columns_synthetic = data['columns_synthetic']
