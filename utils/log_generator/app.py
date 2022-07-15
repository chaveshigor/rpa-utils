from datetime import datetime
from datetime import date
import sys, os

class LogGenerator:

  def __init__(self, bot_name):
    self.log_columns = ['date', 'time', 'error_description', 'error_line', 'current_file', 'dev_description', 'context']
    self.default_path = 'C:/RPA/{}/log.csv'.format(bot_name)
    self.bot_name = bot_name

  def write_log(self):
    pass

  def write_error(self, dev_description='', context=''):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

    self.__create_log_file()

    log_file = open(self.default_path, 'a')
    log_file.write('\n{};{};{};{};{};{};{}'.format(
      date.today().strftime('%d/%m/%Y'),
      datetime.now().strftime('%H:%M:%S'),
      '{} - {}'.format(str(exc_type), str(exc_obj)),
      str(exc_tb.tb_lineno),
      fname,
      str(dev_description),
      str(context)
      )
    )
    log_file.close()

  # Private methods

  def __create_log_file(self):
    folders = os.listdir('C:/')
    if 'RPA' not in folders:
      os.mkdir('C:/RPA')

    folders = os.listdir('C:/RPA')
    if self.bot_name not in folders:
      os.mkdir('C:/RPA/{}'.format(self.bot_name))

    if 'log.csv' not in os.listdir('C:/RPA/{}'.format(self.bot_name)):
      log_file = open(self.default_path, 'w', encoding='utf-8')
      log_file.write(';'.join(self.log_columns))
      log_file.close()
