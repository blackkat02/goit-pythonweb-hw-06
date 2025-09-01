import argparse
from src.database.repository import create_student, get_student

def main():
    parser = argparse.ArgumentParser(description="CLI App for hw_06_db")
    parser.add_argument("-a", "--action", required=True, help="CRUD action: create, read, update, delete")
    parser.add_argument("-m", "--model", required=True, help="Model to work with: Student, Teacher, etc.")
    parser.add_argument("--name", help="Model name")
    parser.add_argument("--group_id", type=int, help="Group ID for a student")

    args = parser.parse_args()

    if args.action == "create":
        if args.model == "Student":
            if args.name and args.group_id:
                create_student(args.name, args.group_id)
                print(f"Student '{args.name}' created successfully with group_id {args.group_id}.")
            else:
                print("Error: Name and group_id are required for creating a student.")
    # Додай логіку для інших дій і моделей

if __name__ == "__main__":
    main()