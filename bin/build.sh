DIR=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
BASEDIR=$DIR/..

VERSION=latest
if [[ "$1" != "" ]]; then
  VERSION=$1
fi

cd $BASEDIR

docker build -f $BASEDIR/docker/Dockerfile -t sohoffice/tempalte-tools:$VERSION .
