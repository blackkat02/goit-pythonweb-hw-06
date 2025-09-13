# import argparse
# import asyncio
# import sys

# from src.handlers import 
from src.handlers.decorators import formatter
# from seed import main as seed_main
# from src.database.db import session_manager
# from src.database.repository import (
#     create_student,
#     create_group,
#     create_subject,
#     create_teacher,
#     create_rating,
#     select_1,
#     select_2,
#     select_3,
#     select_4,
#     select_5,
#     select_6,
#     select_7,
#     select_8,
#     select_9,
#     select_10,
# )


# ---------- SELECT FORMATTERS ----------
@formatter("select_1")
def format_select_1(result, args):
    print("\n📊 Топ-5 студентів з найбільшим середнім балом:")
    for student_name, avg_rating in result:
        print(f"   {student_name}: {avg_rating:.2f}")


@formatter("select_2")
def format_select_2(result, args):
    if result:
        print(
            f"\n🏆 Кращий студент з предмета '{args.subject_name}': {result.student_name}, середній бал: {result.avg_rating:.2f}"
        )
    else:
        print("❌ Студентів за цим предметом не знайдено.")


@formatter("select_3")
def format_select_3(result, args):
    if result:
        print(
            f"\n📚 Середній бал по групі '{args.group_name}': {result.avg_rating:.2f}"
        )
    else:
        print("❌ Групу не знайдено.")


@formatter("select_4")
def format_select_4(result, args):
    if result:
        print(f"\n📈 Середній бал на потоці: {result.avg_rating:.2f}")
    else:
        print("❌ Даних не знайдено.")


@formatter("select_5")
def format_select_5(result, args):
    print(f"\n📘 Курси, які читає викладач '{args.teacher_name}':")
    for r in result:
        print(f"   {r}")


@formatter("select_6")
def format_select_6(result, args):
    print(f"\n👨‍🎓 Студенти у групі '{args.group_name}':")
    for r in result:
        print(f"   {r}")


@formatter("select_7")
def format_select_7(result, args):
    print(
        f"\n📝 Оцінки студентів з групи '{args.group_name}' по предмету '{args.subject_name}':"
    )
    for student_name, rating in result:
        print(f"   {student_name}: {rating}")


@formatter("select_8")
def format_select_8(result, args):
    if result:
        print(
            f"\n📊 Середній бал, який поставив викладач '{args.teacher_name}': {result.avg_rating:.2f}"
        )
    else:
        print("❌ Даних не знайдено.")


@formatter("select_9")
def format_select_9(result, args):
    print(f"\n📘 Курси, які відвідує студент {args.student_id}:")
    for r in result:
        print(f"   {r}")


@formatter("select_10")
def format_select_10(result, args):
    print(
        f"\n📘 Курси, які викладач '{args.teacher_name}' читає студенту {args.student_id}:"
    )
    for r in result:
        print(f"   {r}")