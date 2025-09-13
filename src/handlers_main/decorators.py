# import argparse
# import asyncio
# import sys

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


# ---------- DECORATORS ----------
_COMMAND_HANDLERS = {}
_SELECT_FORMATTERS = {}


def command(name):
    def decorator(func):
        _COMMAND_HANDLERS[name] = func
        return func

    return decorator


def formatter(name):
    def decorator(func):
        _SELECT_FORMATTERS[name] = func
        return func

    return decorator