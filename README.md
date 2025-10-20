# HNG13 Task | Stage 1 | Backend | String Analyzer API — FastAPI

A simple FastAPI service that analyzes strings and provides detailed properties such as word count, palindrome detection, unique characters, and SHA256 hash.  
It also supports **filtering**, **natural language queries**, and **CRUD operations** for stored strings.

This project was built as part of the **HNG13 Internship — Stage 1 Backend Task**.

---

## 🚀 Features

- Analyze any string for:
  - Length  
  - Palindrome detection  
  - Word count  
  - Unique character count  
  - SHA256 hash  
  - Character frequency map
- Store and retrieve analyzed strings from the database
- Filter results via query parameters or **natural language**
- Handles duplicate entries gracefully
- Returns structured JSON responses
- Built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**
- Includes CORS setup for frontend integration

---
## 💻 Tech Stack

- `Backend:` FastAPI

- `Language:` Python

- `HTTP Client:` requests

- `Environment Management:` python-dotenv

- `Deployment:` Railway

---

## 🧩 API Endpoints

| Method | Endpoint | Description |
|:-------|:----------|:-------------|
| **POST** | `/strings` | Analyze and store a string |
| **GET** | `/strings` | Retrieve all strings (with optional filters) |
| **GET** | `/strings/{string_value}` | Retrieve details of a specific string |
| **GET** | `/strings/filter-by-natural-language` | Retrieve strings using plain English filters |
| **DELETE** | `/strings/{string_value}` | Delete a specific string record |

---

### ✅ Example Request — Create / Analyze String

**POST** `/strings`

```json
{
  "value": "Dad"
}

```

### Example Response
```json
{
  "id": "7c1079393a5419a23c26fde0a94f45b939f6935facd5090263dc1e32f47969f3",
  "value": "Dad",
  "properties": {
    "length": 3,
    "is_palindrome": true,
    "unique_characters": 3,
    "word_count": 1,
    "sha256_hash": "7c1079393a5419a23c26fde0a94f45b939f6935facd5090263dc1e32f47969f3",
    "character_frequency_map": {
      "d": 2,
      "a": 1,
    }
  },
  "created_at": "2025-10-20T12:23:41.195727"
}

```

### ✅ Example Request — Natural Language Filtering

**GET** `/strings/filter-by-natural-language?query=strings longer than 3 characters`




### Example Response
```json
{
  "data": [
    {
      "id": "c2ab4c...",
      "value": "banana",
      "properties": {
        "length": 6,
        "is_palindrome": false,
        "unique_characters": 3,
        "word_count": 1,
        "sha256_hash": "c2ab4c...",
        "character_frequency_map": {
          "b": 1,
          "a": 3,
          "n": 2
        }
      },
      "created_at": "2025-10-20T10:15:01.245839"
    }
  ],
  "count": 1,
  "interpreted_query": {
    "original": "strings longer than 3 characters",
    "parsed_filters": {
      "min_length": 4
    }
  }
}


```
---

## ⚙️ Environment variables
- Create a .env file in the project root:
```env
DATABASE_URL=postgresql+psycopg://user:password@localhost/databaseName


```
## Cloning the repository
```bash
git clone https://github.com/404khai/hng13-string-analyzer-fastapi
cd hng13-string-analyzer-fastapi


```
## Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate     # On macOS/Linux
venv\Scripts\activate        # On Windows


```
## List of dependencies - Sample requirements.txt
```txt
fastapi
uvicorn
sqlalchemy
pydantic
python-dotenv
psycopg2-binary


```
## Install dependencies
```bash
pip install -r requirements.txt


``` Create a .env file
```bash
cp .env.example .env


```
## Start the development server
```bash
uvicorn main:app --reload


```
## Live access to endpoint at
```bash
https://hng13-profile-api-django-production.up.railway.app/me
