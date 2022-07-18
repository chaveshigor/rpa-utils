import pytest
import openpyxl
import os

from utils.report_generator.app import ReportGenerator


@pytest.fixture
def initialize_report(tmp_path):
  report = ReportGenerator(
    report_path=r'{}\report.xlsx'.format(tmp_path),
    columns_analytical=['Etapa', 'Início', 'Fim', 'Boletos Processados'],
    columns_synthetic=['Empresa', 'Estabelecimento/Banco', 'Conta', 'Status', 'Observação'],
    bot_name='Bananas de Pijamas'
    )
  report.initialize_report()

  return report


def test_if_template_exists():
  template_folder = r'utils\report_generator\files'
  files = os.listdir(template_folder)
  assert "report.xlsx" in files


def test_initialize_report(initialize_report):
  report = initialize_report
  report_folder = '\\'.join(report.report_path.split('\\')[:-1])
  files = os.listdir(report_folder)
  assert "report.xlsx" in files


# def test_write_analytical(initialize_report):
#   report = initialize_report
#   print(report.bot_name)
#   assert 1 == 2

