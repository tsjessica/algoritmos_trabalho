from bs4 import BeautifulSoup
import requests

# Endereço do site em que vamos fazer o scraping
url = 'https://tribunademinas.com.br/noticias/cultura'

# Realiza uma conexão ao site acima, obtendo uma resposta
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:


    html_content = response.text

    # Carrega o HTML no BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    manchete=soup.find_all('h2',class_='title')
    sub=soup.find_all('p',class_='excerpt')

    for i in range(min(len (manchete),len(sub))):
        m = manchete[i]
        s = sub[i]
        if m and s:
            print(m.text)
            print(s.text)
        

                  

