FROM {{ cookiecutter.base_image }}
MAINTAINER {{ cookiecutter.full_name }} {{ cookiecutter.email }}

# Your build

#ENV BUILD_PACKAGES ca-certificates

#RUN apt-get update && \
#    apt-get install -y --no-install-recommends $BUILD_PACKAGES && \
#    rm -rf /var/lib/apt/lists/*

#CMD ["/your-executable"]

# ===== Metadata ======

# Add Dockerfile
COPY Dockerfile /

# Metadata params
ARG BUILD_DATE
ARG VERSION
ARG VCS_URL
ARG VCS_REF

# Metadata
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="{{ cookiecutter.project_name }}" \
      org.label-schema.vcs-url=$VCS_URL \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vendor="{{ cookiecutter.vendor }}" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0" \
      com.{{ cookiecutter.vendor }}.{{ cookiecutter.project_name }}.docker.dockerfile="/Dockerfile"

