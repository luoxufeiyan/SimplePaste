# SimplePaste

A pastebin website that generates easy-to-read codes.

Demo: http://paste.fledding.com


# Install

First install MySQLDB based on your operation system. For Debian/Ubuntu:
```
sudo apt update
sudo apt install python-mysqldb
```

After that, create a isolate runtime environment for the project, virtualenv recommended.

Clone repo:
```angular2
git clone https://github.com/luoxufeiyan/SimplePaste.git
```
create virtualenv environment
```angular2
pip3 install virtualenv
virtualenv SimplePaste/
source SimplePaste/bin/activate
pip3 install -r requirements.txt
```

import Database schema:
```
    mysql -h127.0.0.1 -u DBNAME -pDBPASSWD -DSimplePaste -P3306 < schema.sql
```

Default username is: admin/admin

Rename secure.py.sample to secure.py, and change the config.

Set up supervisor and gunicorn to serve the project. Here is my supervisor config, please change `myproj` directory to your own directory. 

```angular2
[program:SimplePaste]
directory=/myproj/SimplePaste
command=/myproj/SimplePaste/venv/bin/gunicorn app:app -b localhost:8001
environment=PATH="/myproj/SimplePaste/venv//bin:%(ENV_PATH)s"
autorestart=true
user=nobody
redirect_stderr = true
stdout_logfile_maxbytes = 1MB
stdout_logfile_backups = 5
stdout_logfile = /var/log/supervisor/SimplePaste.log
```

Finally, use your favorite http-server (Apache/Nginx) to proxy this project (should on `localhost:8001`) 