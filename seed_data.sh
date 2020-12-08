rm -rf dayssinceapi/migrations
rm db.sqlite3
python manage.py makemigrations dayssinceapi
python manage.py migrate
python manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata dayssinceuser
python manage.py loaddata wellbeing
python manage.py loaddata journalentries
python manage.py loaddata goals
python manage.py loaddata dayssinceboard
python manage.py loaddata articles
python manage.py loaddata comments



