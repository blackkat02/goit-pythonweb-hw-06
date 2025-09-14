import asyncio
import sys

from src.handlers_main.build_parser import build_parser
from src.handlers_main.decorators import _COMMAND_HANDLERS, command, formatter, _SELECT_FORMATTERS


async def main():
    parser = build_parser()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        return

    args = parser.parse_args()
    try:
        # Викликаємо універсальний обробник і передаємо йому функцію репозиторію
        if args.func:
            if "repo_func" in args:
                await args.func(args.repo_func, args)
            else:
                await args.func(args)
    except Exception as e:
        print(f"❌ Помилка виконання: {e}")


if __name__ == "__main__":
    asyncio.run(main())
