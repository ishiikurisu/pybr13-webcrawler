from selenium import webdriver

def main():
    driver = webdriver.Firefox()
    page = 0
    while page <= 5:
        page += 1
        driver.get('https://kabum.com.br/hardware/memoria-ram?string=&pagina={}&ordem=5&limite=30'.format(str(page)))
        content = driver.find_elements_by_css_selector('span.H-titulo a')
        links_vagas = [x.get_attribute('href') for x in content]
        if len(links_vagas) == 0:
            break
        else:
            for link in links_vagas:
                original = link
                aux = link.split('.br')
                if aux[0] == 'https://www.kabum.com':
                    driver.get(link)
                    titulo = driver.find_element_by_css_selector('.titulo_det').text
                    print(titulo)

    driver.quit()

if __name__ == '__main__':
    main()
