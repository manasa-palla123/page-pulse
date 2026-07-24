Page Pulse

Page Pulse is a production-ready URL auditing service built with FastAPI. It analyzes a website URL and returns useful metadata such as HTTP status, response time, server details, and content type. The project also includes caching, request tracing, rate limiting, logging, automated testing, CI/CD, and cloud deployment.

---

Features

- URL validation
- Asynchronous website auditing
- Response time measurement
- HTTP status inspection
- Content-Type detection
- Server header detection
- Configurable in-memory caching
- Unique Request ID generation
- Structured logging
- Rate limiting
- Automated testing with Pytest
- CI/CD using GitHub Actions
- Cloud deployment using Render

Tech Stack

- Python 3.12
- FastAPI
- HTTPX
- CacheTools
- SlowAPI
- Pytest
- GitHub Actions
- Render

Project Structure

page-pulse/
│
├── app/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   ├── config.py
│   └── main.py
│
├── tests/
├── .github/workflows/
├── requirements.txt
└── README.md

Installation

Clone the repository

bash
git clone <repository-url>

Create virtual environment
bash
python -m venv venv

Activate environment

Windows
bash
venv\Scripts\activate

Install dependencies

bash
pip install -r requirements.txt
run the server

bash
python -m uvicorn app.main:app --reload


API Endpoint

POST /audit/

Example Request

    json
{
  "url": "https://google.com"
}


Example Response

json
{
  "request_id": "xxxx-xxxx",
  "success": true,
  "url": "https://www.google.com/",
  "status_code": 200,
  "response_time_ms": 145.31,
  "content_type": "text/html",
  "server": "gws",
  "cached": false
}


Running Tests

bash
pytest


CI/CD

GitHub Actions automatically runs all tests whenever code is pushed to the repository.

Deployment

The application is deployed on Render.

👩‍💻 Author

Manasa Palla