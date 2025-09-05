# goit-pythonweb-hw-06
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