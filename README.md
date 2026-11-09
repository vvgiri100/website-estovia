# Estovia Properties — Flask Website

## Features
- Responsive Estovia Properties landing page
- Buy, sell, and property-care service sections
- Contact/enquiry form
- Enquiries saved to a local SQLite database (`estovia.db`)
- Mobile navigation menu

## 1. Create and activate a virtual environment

macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:
```bat
python -m venv venv
venv\Scripts\activate
```

## 2. Install dependencies
```bash
pip install -r requirements.txt
```

## 3. Run the website
```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Project structure
```text
estovia_flask/
├── app.py
├── requirements.txt
├── README.md
├── estovia.db          # created automatically after first run
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── main.js
```

## Before deploying
- Replace `SECRET_KEY` in `app.py` with a secure random value stored in an environment variable.
- Turn off Flask debug mode in production.
- Configure HTTPS and a production WSGI server such as Gunicorn.
- Add spam protection and privacy/consent wording to the enquiry form.
- Add your official phone number, email, office address, and verified property listings.
- The contact form currently stores enquiries in SQLite; email notifications are not configured.


## To Run
-   python3 -m venv venv (to create local env where ever running)
    source venv/bin/activate
-   pip install -r requirements.txt
-   python3 app.py


## To Stop and Exit
-   CTRL+C
-   deactivate

## On Server
-   cd /var/www/nestro
-   git clone git@github.com:vvgiri100/website-ESTOVIA.git
-   python3 -m venv venv

## Troubleshooting
-    curl -I http://localhost
      HTTP/1.1 200 OK
      Server: nginx
-    curl -I http://externalIP
      HTTP/1.1 200 OK
      Server: nginx
-    sudo nano /etc/nginx/sites-available/estovia
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
-    cat /etc/nginx/sites-available/estovia
-    sudo nano /etc/systemd/system/estovia.service
[Unit]
Description=ESTOVIA Flask Website
After=network.target

[Service]
User=valapatlav
WorkingDirectory=/var/www/estovia/website-ESTOVIA
Environment="PATH=/var/www/estovia/website-ESTOVIA/venv/bin"
ExecStart=/var/www/estovia/website-ESTOVIA/venv/bin/gunicorn --workers 1 --bind 127.0.0.1:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
-    cat /etc/systemd/system/estovia.service
-    sudo systemctl daemon-reload
-    sudo systemctl enable --now estovia
-    sudo systemctl stop estovia
  
