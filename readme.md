# RPA-Utils
Essa biblioteca tem o objetivo de facilitar o desenvolvimento de RPA's, fornecendo soluções já prontas para algumas ações rotineiras em projetos.

## Geração de relatório anaítico e sintético
Para a extração de relatórios é possível utilizar o objeto <b>ReportGenerator</b>.
<br>
<code>
<br>
from utils.report_generator.app import ReportGenerator
<br/><br/>
generator = ReportGenerator(
  <br/>&emsp; report_path='report.xlsx', 
  <br/>&emsp; columns_analytical=['Etapa', 'Início', 'Fim', 'Boletos Processados'],
  <br/>&emsp; columns_synthetic=['Empresa', 'Estabelecimento/Banco', 'Conta', 'Status', 'Observação'],
  <br/>&emsp; bot_name='Bananas de Pijamas'
  <br/>&emsp; )
</code>

O exemplo acima ilustra a criação de um documento excel com os seguintes relatórios contendo as seguintes colunas:

### Relatório analítico 
- Etapa
- Início
- Fim
- Boletos Processados
### Relatório sintético
- Empresa
- Estabelecimento/Banco
- Conta
- Status
- Observação

Após instanciar o object, é necessário que o arquivo excel seja inicializado. Isso pode ser feito da seguinte forma:
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