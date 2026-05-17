"""Seed data for development and testing."""

import asyncio
from uuid import uuid4
from datetime import datetime, timedelta

from config.database.connection import async_session_maker, engine
from config.database.models import Base, User, NegotiationJob


async def create_tables():
    """Create all database tables."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def seed_users():
    """Create sample users."""
    async with async_session_maker() as session:
        users = [
            User(
                id=uuid4(),
                email="demo@aan.ai",
                username="demo",
                hashed_password="$2b$12$dummy_hash_for_demo",
                full_name="Demo User",
                is_active=True,
                is_superuser=False,
            ),
            User(
                id=uuid4(),
                email="admin@aan.ai",
                username="admin",
                hashed_password="$2b$12$dummy_hash_for_admin",
                full_name="Admin User",
                is_active=True,
                is_superuser=True,
            ),
        ]
        session.add_all(users)
        await session.commit()
        print(f"Created {len(users)} users")


async def seed_jobs():
    """Create sample negotiation jobs."""
    async with async_session_maker() as session:
        jobs = [
            NegotiationJob(
                id=uuid4(),
                user_id=uuid4(),
                product_query="iPhone 15 Pro",
                min_price=2000,
                max_price=4000,
                currency="AED",
                location_city="Dubai",
                location_radius=30,
                urgency="normal",
                status="queued",
            ),
            NegotiationJob(
                id=uuid4(),
                user_id=uuid4(),
                product_query="MacBook Pro M3",
                min_price=5000,
                max_price=8000,
                currency="AED",
                location_city="Abu Dhabi",
                location_radius=50,
                urgency="high",
                status="running",
            ),
        ]
        session.add_all(jobs)
        await session.commit()
        print(f"Created {len(jobs)} jobs")


async def main():
    """Run seed operations."""
    print("Creating tables...")
    await create_tables()
    
    print("Seeding users...")
    await seed_users()
    
    print("Seeding jobs...")
    await seed_jobs()
    
    print("Seed complete!")


if __name__ == "__main__":
    asyncio.run(main())