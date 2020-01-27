PROJETO Django

INTRODUÇÃO

    2. Configuração banco de dados - Postgres

    2.1 No arquivo settings.py, configurar "DATABASES":

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',  # OBS: Não altere essa informação
            'NAME': 'nome_banco_dados',
            'USER': 'usuario',
            'PASSWORD': 'senha',
            'HOST': 'localhost',
            'PORT': 'porta'
        }
    }

    2.2 O Django usa ORM para criar as tabelas no banco de dados. Para gerar a estrutura de tabelas definidas no projeto, dois  comandos devem ser executados:

        python manage.py makemigrations (responsável por gerar as migrações)
        pytohn manage.py migrate (executa a criação das tabelas no banco de dados)

    3. Executar o servidor do Django
        python manage.py runserver

    SE TUDO CORRER BEM, A SEGUINTE MENSAGEM DEVE APERECER NO TERMINAL:

    (venv) C:\PyCharmProject\projeto\previsao_tempo>python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    November 07, 2019 - 17:35:30
    Django version 2.2.7, using settings 'previsao_tempo.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

    3.1 URLs de navegação
    http://127.0.0.1:8000/app/consultar_clima
    http://127.0.0.1:8000/app/consultar_historico
 




