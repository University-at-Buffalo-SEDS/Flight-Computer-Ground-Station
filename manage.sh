#!/bin/sh
FLASK_ENV=development exec pipenv run flask "$@"
