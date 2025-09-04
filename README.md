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