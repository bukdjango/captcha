-include .env

build:
	docker build --tag=test \
	--build-arg BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SITE=${BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SITE} \
	--build-arg BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SECRET=${BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SECRET} \
	--build-arg BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SCORE=${BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SCORE} \
	.

test:
	docker run --rm test python ./runtests.py

install:
	docker run --rm test pip install .

run: build
	docker run -p 8000:8000 --rm -it test python ./manage.py runserver 0.0.0.0:8000

suite: build test install
build-test: build test

.PHONY: dist
dist: build
	docker run --rm --volume=${PWD}:/dockerapp test python setup.py sdist
