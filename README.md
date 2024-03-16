# prototipo_bd
 Protótipo do Bando de Dados do SigQueijaria

# Como rodar o bd ?
 1- clone o repositório
 2- abra na pasta bd_api onde está o arquivo "manage.py"
 3- neste diretório escreva o seguinte comando no terminal: "python manage.py runserver"
 4- Após isso, o servidor deverá ser iniciado no link disponibilizado no terminal. Clique nele.
 5- Em seguida, acesse o site postman.com e clique na opção REST API basics e na parte superior clique no ícone que tem o "+".
 6- Feito isso ele vai pedir para você colocar a URL do servidor, você pode por exemplo digitar: http://127.0.0.1:8000/clientes/ se quizer acessar a tabela de clientes. depois é só clicar no botão azul "Send".
 7- Na pasta atual acesse o diretório "bd_api" e abra o arquivo urls.py e veja todos os caminhos que você pode navegar pela url. Exemplo: http://127.0.0.1:8000/nomeDoCaminho/
