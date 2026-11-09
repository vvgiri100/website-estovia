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
-   python3 -m venv venv
    source venv/bin/activate
-   pip install -r requirements.txt
-   python3 app.py


## To Stop and Exit
-   CTRL+C
-   deactivate