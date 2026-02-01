# Whitespace Trimmer

Single-purpose API. Stateless. Deterministic. Returns JSON only.

## Endpoints
- GET `/health`
- GET `/v1/whitespace-trim?text=`

## Example

Request:
`/v1/whitespace-trim?text=%20%20hello%20%20%20world%20%0A`

Response:
```json
{
  "input": "  hello   world \n",
  "trimmed": "hello world",
  "original_length": 16,
  "trimmed_length": 11
}

Commit each (or all three—either is fine).  

---

## Step 2 — Tell me the commit hash
Reply with the **short hash** (7-ish chars) from the latest commit.

---

## Step 3 — Render deploy (immediately after hash)
We’ll deploy with:
- Root Directory: **blank**
- Build: `pip install -r requirements.txt`
- Start: `uvicorn app:app --host 0.0.0.0 --port $PORT`

---



Response:
```json
{
  "input": "  hello   world \n",
  "trimmed": "hello world",
  "original_length": 16,
  "trimmed_length": 11
}
