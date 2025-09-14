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