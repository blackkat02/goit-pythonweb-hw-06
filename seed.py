import asyncio
import random
from datetime import date
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import faker

from src.database.models import Base, Student, Group, Subject, Teacher, Rating
from src.database.repository import create_student, create_group, create_teacher, create_subject, create_rating

# Налаштування
DATABASE_URL = "postgresql+asyncpg://admin:admin@postgres_db:5432/hw_06_db"

engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)
fake = Faker("uk_UA")

async def seed_data(session: AsyncSession):
    # Створення груп
    groups = [Group(group_name=f"Group {i+1}") for i in range(3)]
    session.add_all(groups)
    await session.commit()
    for group in groups:
        await session.refresh(group)

    # Створення викладачів
    teachers = [Teacher(teacher_name=fake.name()) for _ in range(random.randint(3, 5))]
    session.add_all(teachers)
    await session.commit()
    for teacher in teachers:
        await session.refresh(teacher)

    # Створення предметів
    subjects = [
        Subject(
            subject_name=fake.word(), 
            teacher=random.choice(teachers)
        ) for _ in range(random.randint(5, 8))
    ]
    session.add_all(subjects)
    await session.commit()
    for subject in subjects:
        await session.refresh(subject)
    
    # Створення студентів
    students = [
        Student(
            student_name=fake.first_name(),
            student_last_name=fake.last_name(),
            group=random.choice(groups)
        ) for _ in range(random.randint(30, 50))
    ]
    session.add_all(students)
    await session.commit()
    for student in students:
        await session.refresh(student)

    # Створення оцінок
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(1, 20)):
                rating = Rating(
                    rating=random.randint(1, 12), 
                    student=student, 
                    subject=subject,
                    date=fake.date_between(start_date='-1y', end_date='today')
                )
                session.add(rating)
    await session.commit()
    print("Database seeding completed.")

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as session:
        await seed_data(session)

if __name__ == "__main__":
    asyncio.run(main())