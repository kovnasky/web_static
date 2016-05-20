import multiprocessing

bind = "unix:/home/box/web/etc/gunicorn.sock"
workers = 3
errorlog = '/home/box/web/logs/gunicorn.error.log'
#accesslog = '/home/user/logs/gunicorn.access.log'
#loglevel = 'debug'
proc_name = 'gunicorn_appname'
