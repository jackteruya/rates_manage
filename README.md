
### Para esse projeto:
- Crie um virtual enviroment, ative o mesmo e utilize o seguinte comando para instalar as dependência do projeto. `pip install -r requirements.txt`

- Para inicar a aplicação, após ter clonado o repositorio:
  - $ python manage.py migrate (para gerar as tabelas)
  - $ python manage.py createsuperuser (para acessar o admin)
  - $ python manage.py runserver (para rodar a aplicação)
  - geralmente será aberto o server http://127.0.0.1:8801/
  - mas antes de acessar do grafico, chame o http://127.0.0.1:8801/api/rates/create/10
  
- O banco de dados utilizado default é o sqlite, caso queira alterar o banco para postgress, basta alteara as configurações no arquivo settings.py. Já está com as configurações comentadas, basta descomentar o banco postgres e comentar o sqlite.
- Outra situação, se não tiver o BD postgres instalado e tiver o docker e docker-compose instaldo, já tem um arquivo docker-compose.yml:
  - digite no terminal: $ docker-compose up

- Tests:
  - $ coverage run manage.py test
  - $ coverage report
  - $ coverage html
  - $ cd htmlcov
  - $ python -m http.server 8001

- Caso queira utilizar o celery para as tasks:
    - $ sudo apt install redis-server (instalar o redis)
    - $ redis-cli --version (verificar a versão)
    - $ sudo systemctl status redis (verificar se esta ativo)
    - $ sudo systemctl start redis (para ativar ativar, caso não estiver ativo)
    - $ celery -A quote_management worker --loglevel=INFO  (rodar as tarefas)
    - $ celery -A tarefa flower --address=127.0.0.1 --port=5566 --basic_auth==admin:1234 (interface grafica para ver as tarefas)
    - $ celery -A quote_management beat --loglevel=INFOC (rodar as tarefas agendadas)



