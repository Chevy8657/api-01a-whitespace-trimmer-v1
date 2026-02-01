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
