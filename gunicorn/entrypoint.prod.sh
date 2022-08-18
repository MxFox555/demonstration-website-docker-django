#!/bin/sh

if ["$DATABASE" = "postgres"]
then
	echo "Waiting for postgres..."

	while ! nc -z $SQL_HOST $SQL_PORT; do
		sleep 0.1
	done

	echo "PostgrSQL started"
fi

python manage.py makemigrations
python manage.py migrate

mv staticfiles/bower_components/metisMenu/dist/metismenu.min.css staticfiles/bower_components/metisMenu/dist/metisMenu.min.css
mv staticfiles/bower_components/metisMenu/dist/metismenu.min.js staticfiles/bower_components/metisMenu/dist/metisMenu.min.js

exec "$@"
