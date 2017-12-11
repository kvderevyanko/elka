
Температура
cat /etc/armbianmonitor/datasources/soctemp
cat /sys/devices/virtual/thermal/thermal_zone0/temp

sshfs kirill@192.168.1.29:/ /home/kirill/tmp/


https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-16-04
sudo pip install -U setuptools

uwsgi --http :8080 --home /home/kirill/Env/firstsite --chdir /home/kirill/firstsite -w firstsite.wsgi

[uwsgi]
project = firstsite
uid = kirill
base = /home/%(uid)