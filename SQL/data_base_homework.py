
# 1. Найдите 10 самых часто встречающихся слов.

# Ответ: 
# SELECT plaintext FROM wordform ORDER BY occurences DESC LIMIT(10);

# 2. Найдите все слова, которые начинаются с буквы ‘a’, регистр не должен иметь значения.a’, регистр не должен иметь значения.

# Ответ: 
# SELECT plaintext FROM wordform WHERE stemtext ILIKE 'a%';

# 3. Найдите все произведения, которые относятся к жанру ‘a’, регистр не должен иметь значения.

# Ответ:
# SELECT title, genretype FROM work WHERE genretype LIKE 'p';

# 4. Найдите среднее количество параграфов в произведения жанра ‘a’, регистр не должен иметь значения.

# Ответ:
# SELECT AVG(totalparagraphs) AS avg FROM work WHERE genretype LIKE 't';

# 5. Выведите все произведения, в которых количество слов выше среднего.

# Ответ:
# SELECT title FROM work WHERE totalwords > (SELECT AVG(totalwords) FROM work);

# 6. Выведите имя героя, количество его реплик, и произведение, в котором этот герой встречается.

# Отвтет:
# SELECT character.charname, character.speechcount, work.title FROM character JOIN character_work ON character_work.charid = character.charid JOIN work ON character_work.workid = work.workid;

# 7. Выведите среднее количество реплик героев в произведении ‘a’, регистр не должен иметь значения.Romeo and Juliet’.

# Ответ:
# SELECT ROUND(AVG(character.speechcount)), work.title FROM character JOIN character_work ON character.charid = character_work.charid JOIN work ON work.workid = character_work.workid GROUP BY title HAVING title = 'Romeo and Juliet';

# 8. Выведите общее количество слов в каждой из секций в таблице paragraph.

# Ответ:
# SELECT section, SUM(wordcount) FROM paragraph GROUP BY section;

# 9. Выведите всех героев, которые имеют от 15 до 30 реплик.

# Отвте:
# SELECT charname, speechcount FROM character WHERE speechcount >= 15 AND speechcount <= 30;

# 10. Выведите все произведения, которые были написаны в 17 веке

# Ответ:
# SELECT title, year FROM work WHERE year >= 1601 AND year <= 1700;

# 11. Найдите все произведения, которые имею в полном названии слово ‘a’, регистр не должен иметь значения.the’

# Отвтет:
# SELECT longtitle FROM work WHERE longtitle LIKE '%the%';

# 12. Выведите все уникальные секции в paragraph.

# Ответ:
# SELECT DISTINCT section FROM paragraph;

# 13. Для каждой главы выведите: id, описание и название произведения, к которой относится данная глава.

# Ответ:
# SELECT c.chapterid, c.description, w.title FROM chapter AS c INNER JOIN work AS w ON c.workid = w.workid;

# 14. Для каждого параграфа выведите: номер параграфа, имя героя, и количество реплик героя

# Ответ:
# SELECT paragraph.paragraphnum, character.charname, character.speechcount FROM paragraph JOIN character ON character.charid = paragraph.charid;

# 15. Для каждого параграфа выведите: номер параграфа, название произведения и год выхода этого произведения.

# Ответ:
# SELECT paragraph.paragraphnum, work.title, work.year FROM paragraph JOIN work ON paragraph.workid = work.workid;
