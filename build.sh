#  poetry install

# Comando para instalar as dependências do projeto
pip install -r requirements.txt

# pip install -r requirements.txt

# Comando para criar o banco de dados
python manage.py collectstatic --no-input

# Comando para mirar las tablas a la base de datos
python manage.py migrate