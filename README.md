Curso sobre WebCrawlers
=======================

Sobre
-----

- Ministrado dia 2017.10.10.

Anotações
---------

Um web crawler é um programa que varre informações na internet. A maior dificuldade de se desenvovler um crawler é que as informações não estão padronizadas na internet.

Ferramentas necessárias: Selenium (suite de automação de interfaces gráficas web), um web driver (como o Geckodriver para Firefox). Para instalar o selenium, execute:
```
pip install selenium
```
Assim, já teremos o servidor e um cliente para Python. Para baixar um driver, acesse a [página de downloads do Selenium][1].

O código repassado está no script `main.py`. Aprendemos a manipular elementos; uma técnica para lidar com páginas  `404` não encontradas; e como clicar em botões.

Um exemplo mais completo está no script `hard.py`, onde analisamos um site de compras, andando pelas páginas e analisando os produtos.

Foi comentado no curso que o _driver_ do Selenium tem uma propriedade `driver.status`, que permite checar o código de retorno da página.

[1]: http://www.seleniumhq.org/download/
