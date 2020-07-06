
build:
	docker build --tag=test .

test:
	docker run --rm test python ./runtests.py

install:
	docker run --rm test pip install .


suite: build test install
