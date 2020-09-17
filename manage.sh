#!/bin/sh
FLASK_APP=. FLASK_ENV=development exec pipenv run flask "$@"
