# Setup Instructions for FastAPI Application on DigitalOcean

## 1. Create a DigitalOcean Droplet and SSH into the VM

```bash
ssh root@<ip-addr>
```

## 2. Installations and Checks

- Update and upgrade the system:
  ```bash
  sudo apt update && sudo apt upgrade -y
  ```
- Check Python installation.
- Check pip installation:
  ```bash
  sudo apt install python3-pip
  ```
- Install PostgreSQL:
  ```bash
  sudo apt install postgresql postgresql-contrib
  psql --version
  ```

## 3. PostgreSQL Setup

- Switch to the PostgreSQL user:
  ```bash
  su - postgres
  ```
- Open the PostgreSQL shell:
  ```bash
  psql -U postgres
  ```
- Set the PostgreSQL password:
  ```sql
  \password postgres
  ```
- Update PostgreSQL configuration files:
  ```bash
  cd /etc/postgresql/14/main
  sudo nano postgresql.conf
  ```
  - Under **CONNECTIONS AND AUTHENTICATION**, add:
    ```
    listen_addresses = '*'
    ```
  - Edit `pg_hba.conf` to:
    - Change authentication method to `md5`.
    - Allow all addresses (`0.0.0.0` and `::/0`) for local and host types.
  - Restart PostgreSQL:
    ```bash
    systemctl restart postgresql
    ```

## 4. Create Another User

```bash
adduser <username>
```

## 5. Login as the New User

```bash
ssh <user>@<ip-addr>
```

## 6. Grant Root Access to the New User

Run the following command as `root`:

```bash
usermod -aG sudo <user>
```

Re-login to apply changes.

## 7. Setup the Project

- Create a folder (`app`) and navigate to it.
- Create a virtual environment and a source folder (`src`).
- Clone the repository:
  ```bash
  git clone https://github.com/kanakOS01/social-media-fastapi.git src
  ```

## 8. Setup Environment Variables

- Create a `.env` file in the home directory (`~`).
- Add environment variables to this file.
- Load the variables:
  ```bash
  set -o allexport; source /home/kanak/.env; set +o allexport
  ```
  > **Note**: These variables do not persist through reboots. Add the above command to `.profile`.

## 9. Initialize the Database and Tables

- Create the database.
- Run migrations:
  ```bash
  alembic upgrade head
  ```

## 10. Run the Server

### a. Using FastAPI's Development Server

```bash
fastapi run --app app
```
> **Note**: This is not the best method for production. Use `gunicorn` for better performance.

### b. Using Gunicorn

- Start the server:
  ```bash
  gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app -b 0.0.0.0:8000
  ```
  - `gunicorn`: Start the server.
  - `-w 4`: Use 4 workers.
  - `-k uvicorn.workers.UvicornWorker`: Use Uvicorn worker class.
  - `-b 0.0.0.0:8000`: Bind to all interfaces on port 8000.

### c. Create a Service for Gunicorn

- Navigate to `/etc/systemd/system`:
  ```bash
  cd /etc/systemd/system
  ```
- Create `api.service` and add the Gunicorn configuration.
- Start the service:
  ```bash
  systemctl start api.service
  systemctl status api.service
  ```
- If environment variables are not loaded, add:
  ```
  EnvironmentFile=/home/kanak/.env
  ```
  Restart the service.

### d. Enable the Service to Restart on Reboot

```bash
sudo systemctl enable api
```

## 11. Setup Nginx

- Install Nginx:
  ```bash
  sudo apt install nginx
  ```
- Start the service:
  ```bash
  systemctl start nginx
  ```
- Navigate to Nginx configuration directory:
  ```bash
  cd /etc/nginx/sites-available
  ```
- Add the Nginx configuration file.
- Restart Nginx:
  ```bash
  systemctl restart nginx
  ```

## 12. Configure a Domain Name

- Update name servers: [DigitalOcean Docs](https://docs.digitalocean.com/products/networking/dns/getting-started/dns-registrars/)
- Manage DNS records: [DigitalOcean Docs](https://docs.digitalocean.com/products/networking/dns/how-to/manage-records/)
- Add the following DNS records:
  - **A Record**: Point to your droplet's IP address.
  - **CNAME Record**: Add your desired subdomain.

## 13. SSL/HTTPS
- Go to https://certbot.eff.org/
- Click `Get Certbot instructions`
- follow instructions

## 14. Restrict ports
- setup a firewall to restrict what ports are allowed
- `sudo ufw status`
- allow http, https, ssh
  - `sudo ufw allow http`
  - `sudo ufw allow https`
  - `sudo ufw allow ssh`
- allow postgres (if u want to use database remotely)
  - `sudo ufw allow 5432`
- `sudo ufw enable`
- then reboot

## 15. Docker
- setup docker locally
- to build the image from `Dockerfile` run `docker build -t fastapi .`
- spin container with `docker compose -d`
  > had to go into api container and run `alembic upgrade head` to create the tables, not sure why 
- add to docker hub
  - rename the image - `docker image tag <old name> <new name>
  - `docker push <new name>

## 16. CI/CD

