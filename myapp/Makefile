# use TAB instead of four blank spaces before each command

install:
	# This should be run from inside a virtualenv
	pip install --upgrade pip
	pip install -r requirements.txt

lint:
	hadolint Dockerfile
	pylint --disable=R,C,W1203 myapp.py
	pylint --disable=R,C,W1203 wsgi.py

all: install lint