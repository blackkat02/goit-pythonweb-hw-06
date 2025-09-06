# goit-pythonweb-hw-06

🚀 Getting Started
To run this project, you need to have Docker and Docker Compose installed.

Clone the repository:

Bash

git clone [your_repository_url]
cd [your_repository_folder]
Build and run the Docker containers:

Bash

docker-compose up -d --build
This command will build the Python application image and start the PostgreSQL database and the application containers in the background.

📜 Usage Examples
The application is controlled via the main.py script inside the Docker container. All commands are executed using docker exec.

1. Database Seeding
Use this command to fill the database with sample data. This is the first step you should perform.

Bash

docker exec -it goit-pythonweb-hw-06-app-1 /usr/local/bin/python main.py seed
2. Creating New Entities
Use the create command to add new records to the database.

Create a Student:

Bash

docker exec -it goit-pythonweb-hw-06-app-1 python main.py create -m Student --name Іван --last_name Петров --group_id 1
Create a Teacher:

Bash

docker exec -it goit-pythonweb-hw-06-app-1 python main.py create -m Teacher --name "Марія Іванівна"
3. Executing Select Queries
The application includes predefined queries (select_1 to select_10) to retrieve specific data from the database.

Find the top 5 students with the highest average grade:

Bash

docker exec -it goit-pythonweb-hw-06-app-1 python main.py select_1
Find the best student in a specific subject (e.g., "History"):

Bash

docker exec -it goit-pythonweb-hw-06-app-1 python main.py select_2 --subject_name "History"
Find all students in a specific group (e.g., "Group 1"):

Bash

docker exec -it goit-pythonweb-hw-06-app-1 python main.py select_6 --group_name "Group 1"
Find a list of courses a specific student attends (e.g., student ID 5):

Bash

docker exec -it goit-pythonweb-hw-06-app-1 python main.py select_9 --student_id 5
Find a list of courses a specific teacher teaches a specific student:

Bash

docker exec -it goit-pythonweb-hw-06-app-1 python main.py select_10 --student_id 2 --teacher_name "Марія Іванівна"

🔍 How It Works
The application's logic is structured to separate concerns:

main.py acts as a dispatcher. It uses argparse to parse commands and their arguments.

Handlers (e.g., handle_create, handle_select) contain the core business logic and run the database operations.

Formatters display the results in a human-readable format, keeping the main logic clean.

Repository Functions (in src/database/repository.py) contain the actual SQLAlchemy queries for each select operation.


docker exec -it goit-pythonweb-hw-06-postgres_db-1 psql -U admin -d hw_06_db  -- enter to DB

SELECT student_id, AVG(rating) FROM ratings GROUP BY student_id ORDER BY AVG(rating) DESC LIMIT 5;  -- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT student_id, subject_id, AVG(rating) FROM ratings WHERE subject_id = 1 GROUP BY student_id, subject_id ORDER BY AVG(rating) DESC LIMIT 1;  -- Знайти студента із найвищим середнім балом з певного предмета.
SELECT
    g.group_name,
    s.subject_name,
    AVG(r.rating)
FROM
    ratings AS r
JOIN
    students AS st ON r.student_id = st.id
JOIN
    groups AS g ON st.group_id = g.id
JOIN
    subjects AS s ON r.subject_id = s.id
GROUP BY
    g.group_name,
    s.subject_name
ORDER BY
    g.group_name,
    AVG(r.rating) DESC;  -- Знайти середній бал у групах з певного предмета.
SELECT AVG(rating) FROM ratings;  -- Знайти середній бал на потоці (по всій таблиці оцінок).
SELECT * FROM subjects WHERE teacher_id = 2;  -- Знайти які курси читає певний викладач.
SELECT id, student_name, student_last_name FROM students WHERE group_id = 1;  -- Знайти список студентів у певній групі.
SELECT st.id, st.student_name, st.student_last_name, sub.subject_name, r.rating FROM students as st JOIN ratings AS r ON student_id = st.id JOIN subjects as sub ON r.subject_id = sub.id WHERE group_id = 2 AND subject_id = 3;  -- Знайти оцінки студентів у окремій групі з певного предмета.
SELECT t.id, AVG(r.rating) FROM ratings AS r JOIN subjects AS sub ON sub.id = r.subject_id JOIN teachers AS t ON sub.teacher_id = t.id WHERE teacher_id = 1 GROUP BY t.id;  -- Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT DISTINCT student_id, subject_id FROM ratings WHERE student_id = 5;  -- Знайти список курсів, які відвідує певний студент.
SELECT DISTINCT sub.subject_name FROM ratings AS r JOIN subjects AS sub ON r.subject_id = sub.id WHERE r.student_id = 2 AND sub.teacher_id = 1;  -- Список курсів, які певному студенту читає певний викладач.