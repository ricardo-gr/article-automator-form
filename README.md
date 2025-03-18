# Flask Article Submission App

A Flask web application for article submission with configurable database support.

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
├── config.py
├── main.py
└── requirements.txt
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# For development (SQLite)
export FLASK_CONFIG=development

# For production (MySQL)
export FLASK_CONFIG=production
export DATABASE_URL=mysql://user:password@localhost/dbname
```

4. Run the application:
```bash
python main.py
```

## Database Configuration

- Development: Uses SQLite (configured in `config.py`)
- Production: Uses MySQL (configured via environment variables)

To switch between databases, set the `FLASK_CONFIG` environment variable to either 'development' or 'production'.

## Features

- Article submission
- User management
- OAuth integration
- Configurable database backend 