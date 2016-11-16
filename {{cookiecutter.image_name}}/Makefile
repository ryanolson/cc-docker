BASE_IMAGE ?= {{ cookiecutter.base_image }}
IMAGE_NAME ?= {{ cookiecutter.image_name }}
RELEASE_IMAGE ?= {{ cookiecutter.release_image }}

ifdef APT_CACHE_SERVER
    CACHES = --build-arg http_proxy=http://${APT_CACHE_SERVER}
else
    CACHES =
endif


.PHONY: build release clean distclean


default: build

Dockerfile: Dockerfile.j2
	j2docker --base-image=${BASE_IMAGE} Dockerfile.j2

build: clean Dockerfile
	docker build ${CACHES} -t ${IMAGE_NAME} . 

singularity: build
	docker run \
	    -v /var/run/docker.sock:/var/run/docker.sock -v ${PWD}:/output \
	    --privileged -t --rm singularityware/docker2singularity ${IMAGE_NAME}

release: build
	docker tag ${IMAGE_NAME} ${RELEASE_IMAGE}
	docker push ${RELEASE_IMAGE}

output:
	@echo Docker Image: ${DOCKER_IMAGE}

clean:
	-@rm -f Dockerfile 2> /dev/null
	-@rm -f *.img
	-@docker rm -v `docker ps -a -q -f "status=exited"` 2> /dev/null
	-@docker rmi `docker images -q -f "dangling=true"` 2> /dev/null

distclean: clean
	-@docker rmi ${IMAGE_NAME} 2> /dev/null
	-@docker rmi ${RELEASE_IMAGE} 2> /dev/null

# -- 
# -- # Get the latest commit.
# -- GIT_COMMIT = $(strip $(shell git rev-parse --short HEAD))
# -- 
# -- # Get the version number from the code
# -- CODE_VERSION = $(strip $(shell python version.py))
# -- 
# -- # Find out if the working directory is clean
# -- GIT_NOT_CLEAN_CHECK = $(shell git status --porcelain)
# -- ifneq (x$(GIT_NOT_CLEAN_CHECK), x)
# -- DOCKER_TAG_SUFFIX = -dirty
# -- endif
# -- 
# -- # If we're releasing to Docker Hub, and we're going to mark it with the latest tag, it should exactly match a version release
# -- ifeq ($(MAKECMDGOALS),release)
# -- # Use the version number as the release tag.
# -- DOCKER_TAG = $(CODE_VERSION)
# -- 
# -- ifndef CODE_VERSION
# -- $(error You need to create a VERSION file to build a release)
# -- endif
# -- 
# -- # See what commit is tagged to match the version
# -- VERSION_COMMIT = $(strip $(shell git rev-list $(CODE_VERSION) -n 1 | cut -c1-7))
# -- ifneq ($(VERSION_COMMIT), $(GIT_COMMIT))
# -- $(error echo You are trying to push a build based on commit $(GIT_COMMIT) but the tagged release version is $(VERSION_COMMIT))
# -- endif
# -- 
# -- # Don't push to Docker Hub if this isn't a clean repo
# -- ifneq (x$(GIT_NOT_CLEAN_CHECK), x)
# -- $(error echo You are trying to release a build based on a dirty repo)
# -- endif
# -- 
# -- else
# -- # Add the commit ref for development builds. Mark as dirty if the working directory isn't clean
# -- DOCKER_TAG = $(CODE_VERSION)-$(GIT_COMMIT)$(DOCKER_TAG_SUFFIX)
# -- endif
# -- 
# -- ##
# -- # Modify this code if you want to build on the host
# -- ## 
# -- 
# -- #SOURCES := $(shell find . -name '*.go')
# -- 
# -- #test:
# -- #	go test -v ./...
# -- 
# -- #get-deps:
# -- #	go get -t -v ./...
# -- 
# -- #$(BINARY): $(SOURCES)
# -- #	# Compile for Linux
# -- #	GOOS=linux go build -o $(BINARY)	
# -- 
# -- docker_build: $(BINARY)
# -- 	# Build Docker image
# -- 	docker build \
# --   --build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
# --   --build-arg VERSION=$(CODE_VERSION) \
# --   --build-arg VCS_URL=`git config --get remote.origin.url` \
# --   --build-arg VCS_REF=$(GIT_COMMIT) \
# -- 	-t $(DOCKER_IMAGE):$(DOCKER_TAG) .
# -- 
# -- docker_push:
# -- 	# Tag image as latest
# -- 	docker tag $(DOCKER_IMAGE):$(DOCKER_TAG) $(DOCKER_IMAGE):latest
# -- 
# -- 	# Push to DockerHub
# -- 	docker push $(DOCKER_IMAGE):$(DOCKER_TAG)
# -- 	docker push $(DOCKER_IMAGE):latest
# -- 
# -- clean:
# -- 	-docker rm -v `docker ps -a -q -f status=exited`
# -- 	-docker rmi `docker images -f "dangling=true" -q`
