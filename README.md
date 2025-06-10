# Flask
## Endpoints
- `GET /ping` — health-check
- `POST /submit` — submit JSON: `{ "name": "Kirill", "score": 88 }`
- `GET /results` — list all entries

## Run with Docker
```bash
cp .env.example .env
# заполнить .env файл со своими кредсами
docker-compose up --build
```