import argparse
from database.repository import create_student, get_student#, ...  Імпортуємо функції з репозиторію

def main():
    parser = argparse.ArgumentParser(description="CLI App for University DB")
    parser.add_argument("-a", "--action", required=True, help="CRUD action")
    parser.add_argument("-m", "--model", required=True, help="Model to work with")
    parser.add_argument("--name", help="Model name")
    # Додай інші аргументи для полів

    args = parser.parse_args()

    # Логіка маршрутизації
    if args.action == "create":
        if args.model == "Student":
            # Тут передаємо дані з терміналу до функції репозиторію
            create_student(args.name, ...) 
            print("Student created successfully.")
    # elif args.action == "read":
    #     if args.model == "Student":
            # ... логіка для читання
    # Додай інші if/elif для інших дій і моделей

if __name__ == "__main__":
    main()