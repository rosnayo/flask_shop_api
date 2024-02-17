#para hacer migraciones
flask db init(solo se ejecuta una vez) si ya lo ejecutaste y tienes ya la carpeta migrations creada entonces no debes volver a ejecutarlo

flask db init "crear la base de datos"
flask db migrate -m "Migrando a la nube"
flask db upgrade
pip install -r requirements.txt
