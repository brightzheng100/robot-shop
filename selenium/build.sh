#!/bin/bash

set -euo pipefail

show_usage () {
    cat << EOF
Usage: $(basename "$0") [-f <Docker file>] [-p]
  -f         specify the Docker file, defaults to "Dockerfile"
  -r         optional, specify the repository or retrieve it from .env
  -t         optional, specify the image tag or retrieve it from .env
  -p         a tag to indicate publish to the repository too after the build
  -l         a tag to indicate publish to the repository too after the build as the "latest" version too
  -h         display this help info and exit
Examples:
  ./$(basename "$0")
  ./$(basename "$0") -p
  ./$(basename "$0") -f Dockerfile.arm64 -p
  ./$(basename "$0") -f Dockerfile.arm64 -r brightzheng100 -t 2.1.0-arm64 -p
  ./$(basename "$0") -f Dockerfile.arm64 -r brightzheng100 -t 2.1.0-arm64 -p -l
EOF
}

opt_f='Dockerfile'  # docker file
opt_r=''            # repo
opt_t=''            # tag
opt_p='false'       # push flag
opt_l='false'       # push flag as the latest

while getopts "f:r:t:plh" opt; do
    case $opt in
        f)  opt_f=$OPTARG
            ;;
        r)  opt_r=$OPTARG
            ;;
        t)  opt_t=$OPTARG
            ;;
        p)  
            opt_p='true'
            ;;
        l)  
            opt_l='true'
            ;;
        h)
            show_usage
            exit 0
            ;;
        ?)
            show_usage >&2
            exit 1
            ;;
    esac
done

# get the tag info
eval $(egrep '[A-Z]+=' ../.env)

if [[ ${opt_r} == "" ]]; then
    opt_r=$REPO
fi
if [[ ${opt_t} == "" ]]; then
    opt_t=$TAG
fi

echo "--> Dockerfile: $opt_f"
echo "--> Repo: $opt_r"
echo "--> Tag: $opt_t"
echo "--> Publish: $opt_p"
echo "--> Publish to latest: $opt_l"

docker build -f ${opt_f} -t ${opt_r}/rs-website-load:${opt_t} . && docker tag ${opt_r}/rs-website-load:${opt_t} ${opt_r}/rs-website-load

if [[ "$opt_p" == "true" ]]
then
    echo "--> pushing as: ${opt_r}/rs-website-load:${opt_t}"
    docker push ${opt_r}/rs-website-load:${opt_t}

    if [[ "$opt_l" == "true" ]]
    then
        echo "--> pushing as: ${opt_r}/rs-website-load:latest"
        docker push ${opt_r}/rs-website-load:latest
    fi
fi
