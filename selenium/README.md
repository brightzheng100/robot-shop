# Selenium-based load generator for website monitoring

This is a load generator from an end-user perspective to simulate browser behaviours to generate traffic for website monitoring.

Currently we can build images for both `X86_64`/`AMD64` and `ARM64`/`AARCH64` images.

## Usage

```sh
$ ./build.sh -h
Usage: build.sh [-f <Docker file>] [-p]
  -f         specify the Docker file, defaults to "Dockerfile"
  -r         optional, specify the repository or retrieve it from .env
  -t         optional, specify the image tag or retrieve it from .env
  -p         a tag to indicate publish to the repository too after the build
  -l         a tag to indicate publish to the repository too after the build as the "latest" version too
  -h         display this help info and exit
Examples:
  ./build.sh
  ./build.sh -p
  ./build.sh -f Dockerfile.arm64 -p
  ./build.sh -f Dockerfile.arm64 -r brightzheng100 -t 2.1.0-arm64 -p
  ./build.sh -f Dockerfile.arm64 -r brightzheng100 -t 2.1.0-arm64 -p -l
```

## Build and publish the image

As per the usage, these are some sample commands to build and publish image:

```sh
# Build image only based on repo and tag set in ../.env, with the default Dockerfile
$ ./build.sh

# Build and publish image based on repo and tag set in ../.env, with the default Dockerfile
$ ./build.sh -p

# Build and publish image, with specified Dockerfile.arm64, based on repo and tag set in ../.env
./build.sh -f Dockerfile.arm64 -p

# Build and publish image, with specified Dockerfile.arm64 and tag
./build.sh -f Dockerfile.arm64 -r brightzheng100 -t 2.1.0-arm64 -p

# Build and publish image, with specified Dockerfile.arm64 and tag. This image will be published as "latest" tag too.
./build.sh -f Dockerfile.arm64 -r brightzheng100 -t 2.1.0-arm64 -p -l
```

## Run it locally

```sh
export HOST="<YOUR ROBOT SHOP HOST URL>"
docker run --name rs-website-load -e HOST -d robotshop/rs-website-load
```

> Note: to stop it, run `docker stop rs-website-load`; to delete it, run `docker rm -f rs-website-load`.

## Run it on Kubernetes / OpenShift

> Note: pick and use the right tag

```sh
kubectl -n robot-shop apply -f - <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rs-website-load
  labels:
    service: rs-website-load
spec:
  replicas: 1
  selector:
    matchLabels:
      service: rs-website-load
  template:
    metadata:
      labels:
        service: rs-website-load
    spec:
      containers:
      - name: rs-website-load
        env:
          - name: HOST
            value: "http://web:8080/"
        #image: robotshop/rs-website-load:latest
        image: brightzheng100/rs-website-load:latest
EOF
```
