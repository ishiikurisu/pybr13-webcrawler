import selenium
from selenium import webdriver
import time

def main():
    """
    Procedimento principal deste tutorial. Requer que algum driver esteja rodando em 2o plano.
    """
    # Escolhendo um navegador
    driver = webdriver.Firefox() # ou webdrive.Chrome(), por exemplo
    driver.get('http://www.imdb.com/chart/top')

    # Manipulando os elementos
    dado = driver.find_element_by_id('home_img')
    print(driver.title)
    print(dado)

    mais_dado = driver.find_element_by_css_selector('td.titleColumn a')
    link = mais_dado.get_attribute("href")
    print(link)
    print()

    # Exemplo com _class_
    driver.get('https://produto.mercadolivre.com.br/MLB-750400411-gelateria-e-sorveteira-agratto-sorvetes-com-frutas-127v-_JM')
    nome = driver.find_element_by_class_name('item-title__primary ').text
    print(driver.title)
    print(nome)
    print()
    driver.get('https://produto.mercadolivre.com.br/MLB-793952232-maquina-de-sorvete-acai-e-frozen-yogurt-_JM')
    nome = driver.find_element_by_class_name('item-title__primary ').text
    print(driver.title)
    print(nome)
    print()

    # Lidando com erro 404
    driver.get('http://meu.ifmg.edu.br/corpore.nasdfasdf')
    titulo = driver.title
    print(titulo)
    if titulo.find('404') != -1:
        print('pagina não encontrada')
    else:
        print('weird...')
    print()

    # Fechando o driver
    driver.close()

if __name__ == '__main__':
    main()
