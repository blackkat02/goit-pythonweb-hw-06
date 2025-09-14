from seed import main as seed_main
from src.handlers_main.decorators import command, _SELECT_FORMATTERS,  _COMMAND_HANDLERS  # formatter,
from src.handlers_main.formatters import formatter
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


@command("create")
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
            print(
                f"✅ Оцінка '{args.rating}' для студента {args.student_id} по предмету {args.subject_id} створена."
            )
        else:
            print("❌ Невідома модель для створення.")


@command("seed")
async def handle_seed(args):
    await seed_main()
    print("🌱 База даних успішно заповнена.")


async def handle_select(repo_func, args):
    """
    Універсальний обробник для всіх запитів SELECT.
    Це усуває дублювання коду в окремих функціях handle_select_N.
    """
    print(f"Отримані аргументи: {vars(args)}")

    async with session_manager() as session:
        # Передаємо лише ті аргументи, які потрібні функції репозиторію
        call_kwargs = {
            k: v
            for k, v in vars(args).items()
            if k not in ["func", "action", "repo_func"]
        }
        result = await repo_func(session=session, **call_kwargs)

        formatter_func = _SELECT_FORMATTERS.get(args.action)
        if formatter_func:
            formatter_func(result, args)
        else:
            print("❌ Невідома дія вибірки.")


