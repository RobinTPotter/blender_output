#! /bin/sh

case $1 in

start )
gunicorn -t 4 -b 0.0.0.0:12345 render_server:app > go.log 2>&1 &
echo $! > pid
;;

stop )
echo stopping
if [ -f pid ]
then
kill $(cat pid)
rm pid
else
echo no pid check for gunicorns
fi
;;

debug )
FLASK_APP=render_server FLASK_ENV=development flask run --host=0.0.0.0 --port=12345
;;

*)
echo "usage $0 stop|start|debug"
;;

esac
