# Cookiecutter Template for Dockerfiles

Save time and typing by templating your Dockerfile builds.  The templates can be use to create reusable extensions.

## Requirements

`pip install`:
  - [cookiecutter](https://github.com/audreyr/cookiecutter)
  
## Quickstart

Note: if you don't want to be prompted for the defaults that I have set, like `name`, `email` or want to modify the
url for the `release_image`, you can add a `.cookiecutterrc` file to your home directory.

```
default_context:
  full_name: "Ryan Olson"
  email: "rolson@nvidia.com"
  github_username: "ryanolson"
  base_image: nvcr.io/nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04
  release_image: nvcr.io/nvidian_sas/{{ cookiecutter.image_name }}
abbreviations:
  dockerfile: https://github.com/ryanolson/cc-docker.git
  gh: https://github.com/{0}.git
```

```
MBP:~ ryan$ cookiecutter dockerfile
full_name [Ryan Olson]:
email [rolson@nvidia.com]:
image_name [image_name]: my-project
base_image [nvcr.io/nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04]:
release_image [nvcr.io/nvidian_sas/my-project]:
MBP:~ ryan$ ls my-project/
Dockerfile.j2  Makefile
MBP:~ ryan$ cd my-project/
MBP:my-project ryan$ make
j2docker --base-image=nvcr.io/nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04 Dockerfile.j2
docker build  -t my-project .
Sending build context to Docker daemon  4.608kB
Step 1/2 : FROM nvcr.io/nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04
...
```

## Extending Docker Images

The `Dockerfile.j2` template in the `cc-docker` project can be used as a reuseable template and applied to
multiple Docker images.  To apply the `Dockerfile.j2` to multiple base images, it's as easy as setting a few
environment variables.

For instance, let's say I wanted to apply a bootstrap to a set of dockerfiles.  This bootstrap might container
packages for my developer environment or possible settings for the image to work correctly on my corporate network.

In my `bootstrap` folder created by `cc-docker`:
```
#!/bin/bash

IMAGES=(caffe cntk mxnet tensorflow torch)
REPO=nvcr.io/nvida
VERSION=17.03

for IMAGE in $IMAGES; do
  BASE_IMAGE=$REPO/$IMAGE:$VERSION \
  IMAGE_NAME=my-$IMAGE:$VERSION \
  RELEASE_IMAGE=registry.local/$IMAGE:$VERSION \
  make release
done

# Clean up images from bootstrap system
# Doing this after ensure that the base layers do not get downloaded repeatedly.

for IMAGE in $IMAGES; do
  BASE_IMAGE=$REPO/$IMAGE:$VERSION \
  IMAGE_NAME=my-$IMAGE:$VERSION \
  RELEASE_IMAGE=registry.local/$IMAGE:$VERSION \
  make distclean
done
```
