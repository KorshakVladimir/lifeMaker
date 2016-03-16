from fabric.api import local

def migrate():
	local('./manage.py makemigrations')
	local('./manage.py migrate')