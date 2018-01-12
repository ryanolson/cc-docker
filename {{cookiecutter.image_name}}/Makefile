BASE_IMAGE ?= {{ cookiecutter.base_image }}
IMAGE_NAME ?= {{ cookiecutter.image_name }}
RELEASE_IMAGE ?= {{ cookiecutter.release_image }}

APT_PROXY ?= "false"
CACHE="RUN echo 'Acquire::HTTP::Proxy \"${APT_PROXY}\";' >> /etc/apt/apt.conf.d/01proxy"

.PHONY: build tag push release clean distclean

default: clean build

build: 
	@echo FROM ${BASE_IMAGE} > .Dockerfile
	@echo ${CACHE} >> .Dockerfile
	@cat Dockerfile >> .Dockerfile
	@echo "RUN rm -f /etc/apt/apt.conf.d/01proxy" >> .Dockerfile
	docker build -t ${IMAGE_NAME} -f .Dockerfile . 

tag: build
	docker tag ${IMAGE_NAME} ${RELEASE_IMAGE}

push: tag
	docker push ${RELEASE_IMAGE}

release: push

clean:
	@rm -f .Dockerfile 2> /dev/null ||:
	@docker rm -v `docker ps -a -q -f "status=exited"` 2> /dev/null ||:
	@docker rmi `docker images -q -f "dangling=true"` 2> /dev/null ||:

distclean: clean
	@docker rmi ${BASE_IMAGE} 2> /dev/null ||:
	@docker rmi ${IMAGE_NAME} 2> /dev/null ||:
	@docker rmi ${RELEASE_IMAGE} 2> /dev/null ||:
