BASE_IMAGE ?= {{ cookiecutter.base_image }}
IMAGE_NAME ?= {{ cookiecutter.image_name }}
RELEASE_IMAGE ?= {{ cookiecutter.release_image }}

ifdef http_proxy
  CACHES = --build-arg http_proxy=${http_proxy} --build-arg https_proxy=${https_proxy}
else
  CACHES =
endif

.PHONY: build tag push release clean distclean

default: clean build

Dockerfile: Dockerfile.j2
	echo FROM ${BASE_IMAGE} > Dockerfile
	cat Dockerfile.j2 >> Dockerfile

build: Dockerfile
	docker build ${CACHES} -t ${IMAGE_NAME} . 

tag: build
	docker tag ${IMAGE_NAME} ${RELEASE_IMAGE}

push: tag
	docker push ${RELEASE_IMAGE}

release: push

clean:
	@rm -f Dockerfile 2> /dev/null ||:
	@docker rm -v `docker ps -a -q -f "status=exited"` 2> /dev/null ||:
	@docker rmi `docker images -q -f "dangling=true"` 2> /dev/null ||:

distclean: clean
	@docker rmi ${IMAGE_NAME} 2> /dev/null ||:
	@docker rmi ${RELEASE_IMAGE} 2> /dev/null ||:
