# RPA-Utils
Essa biblioteca tem o objetivo de facilitar o desenvolvimento de RPA's, fornecendo soluções já prontas para algumas ações rotineiras em projetos.

## Geração de relatório analítico e sintético
Para a geração de relatórios é possível utilizar o objeto <b>ReportGenerator</b>.
```python
from utils.report_generator.app import ReportGenerator

generator = ReportGenerator(
  report_path='report.xlsx',
  columns_analytical=['Etapa', 'Início', 'Fim', 'Boletos Processados'],
  columns_synthetic=['Empresa', 'Estabelecimento/Banco', 'Conta', 'Status', 'Observação'],
  bot_name='Bananas de Pijamas'
  )
```

O exemplo acima ilustra a criação de um documento excel com os seguintes relatórios contendo as seguintes colunas:
<b>
- Relatório analítico: Etapa, Início, Fim, Boletos Processados
- Relatório sintético: Empresa, Estabelecimento/Banco, Conta, Status, Observação
</b>


Após instanciar o objeto, é necessário que o arquivo excel seja inicializado. Isso pode ser feito da seguinte forma:
<code>
<br>
generator.initialize_report()
</code>

Para preencher os relatórios podem ser utilizados alguns métodos:
### write_analytical
<code>
generator.write_analytical({ 'Etapa': 'extração de notas', 'Fim': '10-03-22 05:52:09' })
<br>
</code>
O código acima irá gerar uma nova linha no relatório com as colunas 'Etapa' e 'Fim' preenchidas com os valores passados como parâmetro
