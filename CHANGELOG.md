# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-05-17

### Added
- Multi-platform scraper support (Dubizzle, OLX, Facebook, Amazon, Noon)
- AI-powered negotiation with adaptive strategies
- FastAPI REST API with Swagger documentation
- PostgreSQL database with SQLAlchemy ORM
- Celery workers for background tasks
- Rate limiting with slowapi
- Type checking with MyPy
- Pre-commit hooks configuration
- Code coverage enforcement (70% threshold)
- Database health checks
- Prometheus metrics endpoint
- Comprehensive test suite (31 tests)
- Frontend Vue.js landing page
- React Native mobile app
- Dependabot auto-merge configuration

### Fixed
- CI test enforcement (removed `|| true`)
- Price extraction regex patterns
- Seller classification logic
- pytest.ini configuration

### Changed
- Updated CI workflow with MyPy and coverage
- Improved code quality with Ruff linter
- Added SEO and mobile optimizations to frontend

### Security
- Added rate limiting to API endpoints
- Added CORS configuration

## [0.0.1] - 2026-04-28

### Added
- Initial project setup
- Basic scraper implementations
- Simple negotiation logic
- Docker Compose configuration