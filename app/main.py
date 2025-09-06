from functools import wraps

def cache(func):
    storage = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Формуємо ключ із позиційних та ключових аргументів
        key = args + tuple(sorted(kwargs.items()))
        if key in storage:
            print("Getting from cache")
            return storage[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[key] = result
        return result

    return wrapper

