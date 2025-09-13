import argparse
# import asyncio
# import sys

# from seed import main as seed_main
from src.handlers.handlers import _COMMAND_HANDLERS, handle_select
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

# ---------- BUILDER AND MAIN ----------
def build_parser():
    parser = argparse.ArgumentParser(description="🎓 CLI App for hw_06_db")
    subparsers = parser.add_subparsers(dest="action", help="Дія")

    # Seed command
    seed_parser = subparsers.add_parser(
        "seed", help="Заповнити базу даних випадковими даними"
    )
    seed_parser.set_defaults(func=_COMMAND_HANDLERS["seed"])

    # Create command
    create_parser = subparsers.add_parser("create", help="Створити нову сутність")
    create_parser.add_argument(
        "-m",
        "--model",
        required=True,
        choices=["Student", "Teacher", "Group", "Subject", "Rating"],
        help="Модель для створення",
    )
    create_parser.add_argument("--name", help="Ім'я")
    create_parser.add_argument("--last_name", help="Прізвище")
    create_parser.add_argument("--group_id", type=int, help="ID групи")
    create_parser.add_argument("--teacher_id", type=int, help="ID викладача")
    create_parser.add_argument("--student_id", type=int, help="ID студента")
    create_parser.add_argument("--subject_id", type=int, help="ID предмета")
    create_parser.add_argument("--rating", type=int, help="Оцінка")
    create_parser.set_defaults(func=_COMMAND_HANDLERS["create"])

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

        # Тут ми передаємо універсальний обробник і функцію репозиторію
        sp.set_defaults(func=handle_select, repo_func=globals()[f"select_{i}"])

    return parser