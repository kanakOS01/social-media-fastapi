1. create DO droplet and ssh into the vm using
`ssh root@<ip-addr>`

2. installs and checks
- `sudo apt update && sudo apt upgrade -y`
- check python installation
- check pip installation
	`sudo apt install python3-pip`
- install postgres
	`sudo apt install postgresql postgresql-contrib`
	`psql version`

3. postgres setup
- use postgres user 
	`su - postgres`
- open psql shell
	`psql -U postgres`
- add password
	`\password postgres`
- update postgres files
	`cd /etc/postgresql/14/main`
	- `sudo nano postgresql.conf`
		go to CONNECTIONS AND AUTHENTICATION and add this line to access db with pgadmin remotely
		this is not the most secure 
		`listen_addresses = '*'

	- `sudo nano pg_hba.conf`
		change db access method from peer to md5
		change addresses to all addresses (0.0.0.0 and ::/0) for local and host type
	- restart using `systemctl restart postgresql`
	- now you can connect to psql without changing user to postgres and use a password and check the data remotely

4. create another user
`adduser <username>`

5. login as another user
`ssh <user>@<ip-addr>`

6. give <user> root access
run `usermod -aG sudo <user>` as root and re login

7. setup project
 a. create a folder (app) and cd
 b. create a venv and a folder (src)
 c. `git clone https://github.com/kanakOS01/social-media-fastapi.git src`

8. setup .env
 a. create a `.env` in `~`
 b. add env var in the file
 c. run `set -o allexport; source /home/kanak/.env; set +o allexport`
 > these do not persist throught reboot so add the command to `.profile`

9. initiate database and tables
 a. create the database
 b. run `alembic upgrade head`

10. run the server
 a. `fastapi run --app app`
	not the best method, user gunicorn with workers and persisting server
 b. using gunicorn
	`gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app -b 0.0.0.0:8000`
	gunicorn, 4 workeres, loc of app - app.main:app, bind to 0.0.0.0:8000
 c. create a service
	`cd /etc/systemd/system`
	create api.service
	copy gunicorn.service in this file
 d. run the service
	`systemctl start api.service`
	`systemctl status api.service`
	there will be an error due to env variable as var loaded from .profile can't be accessed from service
	add EnvironmentFile=/home/kanak/.env to api.service file and restart
 e. handle reboot
	if Loaded:  ... disabled then won't restart on reboot
	`sudo systemctl enable api`

11. setup nginx
 a. `sudo apt install nginx`
 b. `systemctl start nginx`
 c. `cd /etc/nginx/sites-available`
 d. add content of nginx file
 e. `systemctl restart nginx`

12. domain name
 a. update name servers - https://docs.digitalocean.com/products/networking/dns/getting-started/dns-registrars/
 b. https://docs.digitalocean.com/products/networking/dns/how-to/manage-records/
 c. add A record
 d. add CNAME record
