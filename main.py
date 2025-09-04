import argparse
import asyncio
import sys
import shlex

from seed import main as seed_main
from src.database.db import session_manager
from src.database.repository import (
    create_student,
    create_group,
    create_subject,
    create_teacher,
    create_rating,
    select_1,
    select_2,
    select_3,
    select_4,
    select_5,
    select_6,
    select_7,
    select_8,
    select_9,
    select_10,
)


# ---------- HANDLERS ----------
async def handle_create(args):
    async with session_manager() as session:
        if args.model == "Student":
            await create_student(args.name, args.last_name, args.group_id, session)
            print(f"✅ Студент '{args.name} {args.last_name}' створений.")
        elif args.model == "Group":
            await create_group(args.name, session)
            print(f"✅ Група '{args.name}' створена.")
        elif args.model == "Teacher":
            await create_teacher(args.name, session)
            print(f"✅ Викладач '{args.name}' створений.")
        elif args.model == "Subject":
            await create_subject(args.name, args.teacher_id, session)
            print(f"✅ Предмет '{args.name}' створений.")
        elif args.model == "Rating":
            await create_rating(args.student_id, args.subject_id, args.rating, session)
            print(f"✅ Оцінка '{args.rating}' для студента {args.student_id} по предмету {args.subject_id} створена.")
        else:
            print("❌ Невідома модель для створення.")


async def handle_select(args):
    async with session_manager() as session:
        repo_func = globals()[args.func.__name__]
        call_kwargs = {k: v for k, v in vars(args).items() if k not in ['func', 'action']}
        result = await repo_func(session, **call_kwargs)

        formatter_func = SELECT_FORMATTERS.get(args.action)
        if formatter_func:
            formatter_func(result, args)
        else:
            print("❌ Невідома дія вибірки.")


async def handle_seed(args):
    await seed_main()
    print("🌱 База даних успішно заповнена.")


# ---------- SELECT FORMATTERS ----------
def format_select_1(result, args):
    print("\n📊 Топ-5 студентів з найбільшим середнім балом:")
    for student_name, avg_rating in result:
        print(f"   {student_name}: {avg_rating:.2f}")


def format_select_2(result, args):
    if result:
        print(f"\n🏆 Кращий студент з предмета '{args.subject_name}': {result.student_name}, середній бал: {result.avg_rating:.2f}")
    else:
        print("❌ Студентів за цим предметом не знайдено.")


def format_select_3(result, args):
    if result:
        print(f"\n📚 Середній бал по групі '{args.group_name}': {result.avg_rating:.2f}")
    else:
        print("❌ Групу не знайдено.")


def format_select_4(result, args):
    if result:
        print(f"\n📈 Середній бал на потоці: {result.avg_rating:.2f}")
    else:
        print("❌ Даних не знайдено.")


def format_select_5(result, args):
    print(f"\n📘 Курси, які читає викладач '{args.teacher_name}':")
    for r in result:
        print(f"   {r}")


def format_select_6(result, args):
    print(f"\n👨‍🎓 Студенти у групі '{args.group_name}':")
    for r in result:
        print(f"   {r}")


def format_select_7(result, args):
    print(f"\n📝 Оцінки студентів з групи '{args.group_name}' по предмету '{args.subject_name}':")
    for student_name, rating in result:
        print(f"   {student_name}: {rating}")


def format_select_8(result, args):
    if result:
        print(f"\n📊 Середній бал, який поставив викладач '{args.teacher_name}': {result.avg_rating:.2f}")
    else:
        print("❌ Даних не знайдено.")


def format_select_9(result, args):
    print(f"\n📘 Курси, які відвідує студент {args.student_id}:")
    for r in result:
        print(f"   {r}")


def format_select_10(result, args):
    print(f"\n📘 Курси, які викладач '{args.teacher_name}' читає студенту {args.student_id}:")
    for r in result:
        print(f"   {r}")


# ---------- DISPATCHER ----------
ACTION_HANDLERS = {
    "create": handle_create,
    "seed": handle_seed,
    "select_1": handle_select,
    "select_2": handle_select,
    "select_3": handle_select,
    "select_4": handle_select,
    "select_5": handle_select,
    "select_6": handle_select,
    "select_7": handle_select,
    "select_8": handle_select,
    "select_9": handle_select,
    "select_10": handle_select,
}

SELECT_FORMATTERS = {
    "select_1": format_select_1,
    "select_2": format_select_2,
    "select_3": format_select_3,
    "select_4": format_select_4,
    "select_5": format_select_5,
    "select_6": format_select_6,
    "select_7": format_select_7,
    "select_8": format_select_8,
    "select_9": format_select_9,
    "select_10": format_select_10,
}


def build_parser():
    parser = argparse.ArgumentParser(description="🎓 CLI App for hw_06_db")
    subparsers = parser.add_subparsers(dest="action", help="Дія")

    # Seed
    seed_parser = subparsers.add_parser("seed", help="Заповнити базу даних випадковими даними")
    seed_parser.set_defaults(func=ACTION_HANDLERS["seed"])

    # Create
    create_parser = subparsers.add_parser("create", help="Створити нову сутність")
    create_parser.add_argument("-m", "--model", required=True, choices=["Student", "Teacher", "Group", "Subject", "Rating"], help="Модель для створення")
    create_parser.add_argument("--name", help="Ім'я")
    create_parser.add_argument("--last_name", help="Прізвище")
    create_parser.add_argument("--group_id", type=int, help="ID групи")
    create_parser.add_argument("--teacher_id", type=int, help="ID викладача")
    create_parser.add_argument("--student_id", type=int, help="ID студента")
    create_parser.add_argument("--subject_id", type=int, help="ID предмета")
    create_parser.add_argument("--rating", type=int, help="Оцінка")
    create_parser.set_defaults(func=ACTION_HANDLERS["create"])

    # Select queries
    for i in range(1, 11):
        sp = subparsers.add_parser(f"select_{i}", help=f"Виконати select_{i}")
        if i == 2:
            sp.add_argument("--subject_name", required=True, help="Назва предмета")
        elif i == 3:
            sp.add_argument("--group_name", required=True, help="Назва групи")
        elif i == 5:
            sp.add_argument("--teacher_name", required=True, help="Ім'я викладача")
        elif i == 6:
            sp.add_argument("--group_name", required=True, help="Назва групи")
        elif i == 7:
            sp.add_argument("--group_name", required=True, help="Назва групи")
            sp.add_argument("--subject_name", required=True, help="Назва предмета")
        elif i == 8:
            sp.add_argument("--teacher_name", required=True, help="Ім'я викладача")
        elif i == 9:
            sp.add_argument("--student_id", type=int, required=True, help="ID студента")
        elif i == 10:
            sp.add_argument("--student_id", type=int, required=True, help="ID студента")
            sp.add_argument("--teacher_name", required=True, help="Ім'я викладача")

        sp.set_defaults(func=ACTION_HANDLERS[f"select_{i}"])

    return parser


async def interactive_loop(parser):
    print("💡 Інтерактивний режим CLI (введіть 'exit' для виходу)")
    while True:
        try:
            command = input(">>> ")
            if command.strip().lower() in {"exit", "quit"}:
                print("👋 Вихід...")
                break
            if not command.strip():
                continue

            args = parser.parse_args(shlex.split(command))
            await args.func(args)
        except SystemExit:
            # argparse викликає SystemExit при помилках..
            continue
        except Exception as e:
            print(f"❌ Помилка: {e}")


async def main():
    parser = build_parser()
    # if len(sys.argv) == 1:
    #     # Якщо немає аргументів → запускаємо інтерактивний режим
    #     await interactive_loop(parser)
    #     # return
    # else:
    args = parser.parse_args()
    await args.func(args)


if __name__ == "__main__":
    asyncio.run(main())
