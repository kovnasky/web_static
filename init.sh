sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/ask
sudo ln -sf /home/box/web/hello.py /etc/gunicorn.d/hello.py
cd /home/box/web/
gunicorn -b 0.0.0.0:8080 -D hello:app
cd /home/box/web/ask/
gunicorn ask.wsgi:application --bind 0.0.0.0:8000 -D
sudo /etc/init.d/nginx restart
