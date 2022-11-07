dev:
	cd /home/docker/code/app
	echo "Sleeping a 5 seconds so that postgres will (hopefully) be up." && sleep 5
	python manage.py migrate -s public
	python manage.py migrate
	/usr/local/bin/python manage.py collectstatic --noinput
	python manage.py bootstrap_data

	python manage.py createsuperuser --noinput > /dev/null & # We don't care about this result as it will only run successfully the first time
	python manage.py runserver 0.0.0.0:8000

tail:
	tail -f /dev/null

