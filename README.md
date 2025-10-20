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
- Built with **FastAPI**, **SQLAlchemy**, and **SQLite/PostgreSQL**
- Includes CORS setup for frontend integration

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

### ✅ Example Request — Analyze String

**POST** `/strings`

```json
{
  "value": "Dad"
}

Example Response
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
      "D": 1,
      "a": 1,
      "d": 1
    }
  },
  "created_at": "2025-10-20T12:23:41.195727"
}
