IMAGE_NAME = python3

default: run

build:
	docker build --tag=$(IMAGE_NAME) .

run: build
	docker run -d $(IMAGE_NAME)

test: # build  # TODO disabled until building of the Python module is implemented
	cd tests; MODULE=docker make all
	# cd tests; MODULE=rpm make all  # TODO Disabled until Python module is built
