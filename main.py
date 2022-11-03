from utils import get_int_from_str, get_str_from_int


def main():
    while (expression := input("Введите выражение: ")) is not None:
        result = get_int_from_str(expression)
        str_result = get_str_from_int(result)
        print(f"Результат выражения: {str_result}.")
        print()

        
if __name__ == "__main__":
    main()