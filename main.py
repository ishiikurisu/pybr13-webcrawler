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
    time.sleep(5)
    driver.close()

if __name__ == '__main__':
    main()
