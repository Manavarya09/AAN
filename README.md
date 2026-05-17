# Autonomous AI Negotiator (AAN)

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/python-3.11+-green" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-orange" alt="License">
</p>

An AI-powered system that discovers deals across online marketplaces and autonomously negotiates with sellers to get the best price.

## Features

- **Multi-Platform Search**: Aggregate listings from Dubizzle, OLX, Facebook Marketplace, Noon, and Amazon.ae
- **Adaptive Negotiation**: AI agents adapt to seller behavior (low anchor, bundle, fair value strategies)
- **Intelligent Scoring**: Weighted ranking by price, condition, location, negotiability, and recency
- **Parallel Threads**: Negotiate with 10+ sellers simultaneously
- **Auto-Close**: Automatically accept when a deal hits your target
- **Outcome Learning**: System learns from every negotiation

## Tech Stack

### Backend
- **Framework**: FastAPI
- **Task Queue**: Celery with Redis
- **Database**: PostgreSQL (async with SQLAlchemy)
- **AI**: LiteLLM (GPT-4o, Claude)
- **Scraping**: Playwright with stealth mode

### Frontend
- Vue 3 + Vite
- React Native (Mobile)

### Infrastructure
- Docker + Docker Compose
- Railway (Deployment)

## Project Structure

```
AAN/
├── services/
│   ├── api/              # FastAPI REST API
│   │   ├── main.py       # App entry point
│   │   └── routes/       # API endpoints
│   └── worker/           # Celery workers
│       ├── scrapers/     # Platform scrapers
│       ├── negotiation/  # AI negotiation agents
│       └── tasks/        # Background tasks
├── config/
│   ├── core/             # Settings
│   ├── database/         # Models & schemas
│   └── scrapers/         # Platform configs
├── tests/
│   ├── unit/             # Unit tests (31 tests)
│   └── integration/      # API tests
├── frontend/             # Vue.js landing page
└── mobile/               # React Native app
```

## Quick Setup

### Prerequisites
- Python 3.11+
- Docker & Docker Compose
- Node.js 20+ (for frontend)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Manavarya09/AAN.git
cd AAN
```

2. Install Python dependencies:
```bash
pip install -e ".[dev]"
```

3. Copy environment file:
```bash
cp .env.example .env
```

4. Start with Docker Compose:
```bash
docker-compose up -d
```

### Development Server

API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

Frontend: http://localhost:5173

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=config --cov=services --cov-report=term-missing
```

### Running Linting

```bash
ruff check config/ services/
mypy config/ services/ --ignore-missing-imports
```

## API Endpoints

- `GET /` - API info
- `GET /health` - Health check (includes DB status)
- `GET /docs` - Swagger documentation
- `GET /metrics` - Prometheus metrics
- `POST /api/v1/jobs` - Create negotiation job
- `GET /api/v1/jobs` - List jobs
- `GET /api/v1/listings` - Get normalized listings
- `GET /api/v1/analytics` - Analytics data

## Contributing

1. Create a feature branch
2. Make changes and add tests
3. Run linting and tests
4. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

For issues and questions, please open a GitHub issue.