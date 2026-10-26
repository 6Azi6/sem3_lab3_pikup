from functools import wraps


def print_result(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        print(function.__name__)

        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)

        return result

    return wrapper


@print_result
def test_number():
    return 1


@print_result
def test_text():
    return "Python"


@print_result
def test_dict():
    return {"a": 1, "b": 2}


@print_result
def test_list():
    return [1, 2]


if __name__ == "__main__":
    test_number()
    test_text()
    test_dict()
    test_list()
