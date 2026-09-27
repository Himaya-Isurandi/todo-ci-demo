# Todo CI Demo

## Setup
Run the app locally with: `uvicorn main:app --reload`
Run tests with: `pytest`

## Secrets
The `DB_URL` secret must live in GitHub Actions secrets and never be committed. See `.env.example` for local setup.

## Branching
feature/* -> dev -> staging -> main
