import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker

from src.database.models import Base, Student, Group
from src.database.repository import create_student, create_group

# Вкажи тут свій рядок підключення до бази даних
DATABASE_URL = "postgresql+asyncpg://admin:admin@localhost:5432/hw_06_db"

engine = create_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)
fake = Faker()

async def seed_data():
    async with async_session() as session:
        print("Creating groups...")
        group_names = ["Group A", "Group B", "Group C"]
        groups = [await create_group(session, name) for name in group_names]

        print("Creating 50 students...")
        for _ in range(50):
            await create_student(session, fake.name(), fake.random_element(elements=[g.id for g in groups]))
            
        print("Creating 50 teachers...")
        # TODO: Додай логіку для створення 50 вчителів

        print("Creating subjects and grades...")
        # TODO: Додай логіку для створення предметів і оцінок

async def main():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
    
    await seed_data()
    print("Database seeding completed!")

if __name__ == "__main__":
    asyncio.run(main())