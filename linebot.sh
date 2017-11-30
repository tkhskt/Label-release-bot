#!/bin/sh
PROGNAME=`basename $0`
BASEDIR=`dirname $0`
PIDFILE=$BASEDIR/$PROGNAME.pid

start() {
  echo "Starting server..."
  cd $BASEDIR
  gunicorn linebot.wsgi --bind=0.0.0.0:8000 -D
}

stop() {
  echo "Stopping server..."
  pkill -TERM `cat $PIDFILE`
  rm -f $PIDFILE
}

usage() {
  echo "usage: $PROGNAME start|stop|restart"
}

if [ $# -lt 1 ];  then
  usage
  exit 255
fi

case $1 in
  start)
    start
    ;;
  stop)
    stop
    ;;
  restart)
    stop
    start
    ;;
esac
