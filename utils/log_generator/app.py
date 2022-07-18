from utils.bot_info.app import BotInfo

from datetime import datetime
from datetime import date
import sys, os

class LogGenerator:

  def __init__(self, show_logs=False):
    self.bot_info = BotInfo()
    self.bot_name = self.bot_info.name
    self.execution_id = self.bot_info.execution_id
    self.show_logs = show_logs
    self.log_columns = ['execution_id', 'date', 'time', 'error_description', 'error_line', 'current_file', 'dev_description', 'context']
    self.default_path = 'C:/RPA/{}/log.csv'.format(self.bot_name)

  def write_log(self, current_file, dev_description, context = ''):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    error_line = ''
    error_description = ''
    if exc_tb:
      error_line = exc_tb.tb_lineno
      error_description = '{} {}'.format(str(exc_type), str(exc_obj))
    # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

    self.__create_log_file()

    log_file = open(self.default_path, 'a')
    log_file.write('\n{};{};{};{};{};{};{};{}'.format(
      str(self.execution_id),
      date.today().strftime('%d/%m/%Y'),
      datetime.now().strftime('%H:%M:%S:%f'),
      error_description,
      str(error_line),
      str(current_file),
      str(dev_description),
      str(context)
      )
    )
    log_file.close()

    if self.show_logs:
      print('>> {}'.format(dev_description))

  def write_error(self, current_file, dev_description='', context=''):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

    self.__create_log_file()

    log_file = open(self.default_path, 'a')
    log_file.write('\n{};{};{};{};{};{};{};{}'.format(
      str(self.execution_id),
      date.today().strftime('%d/%m/%Y'),
      datetime.now().strftime('%H:%M:%S:%f'),
      '{} {}'.format(str(exc_type), str(exc_obj)),
      str(exc_tb.tb_lineno),
      str(current_file),
      str(dev_description),
      str(context)
      )
    )
    log_file.close()

    if self.show_logs:
      print('>> Error: {} - {} - {}'.format(dev_description))


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
