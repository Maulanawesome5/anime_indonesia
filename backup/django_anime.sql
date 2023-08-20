-- Active: 1667427687682@@localhost@3306@django_anime

SELECT VERSION();
USE django_anime;
SHOW TABLES;

SELECT * FROM animelist_anime; SELECT * FROM animelist_studio;
DROP TABLE animelist_anime; DROP TABLE animelist_studio;

SELECT * FROM animelist_anime ORDER BY anime_title ASC;
SELECT * FROM animelist_anime ORDER BY LENGTH(anime_title) DESC;
DESCRIBE animelist_anime; DESCRIBE animelist_studio;

SELECT
    mal_id AS MAL_ID,
    anime_title AS TITLE,
    LENGTH(anime_title) AS LEN_JUDUL
FROM animelist_anime ORDER BY LENGTH(anime_title) DESC;

SELECT * FROM animelist_studio ORDER BY studio_name ASC;

-- ======================================================
-- Query Join tabel anime, studio, dan genre anime
-- ======================================================
SELECT
    animelist_anime.anime_title AS "Judul Anime",
    animelist_anime.anime_score AS "Score Anime",
    animelist_anime.airing_time AS "Musim Rilis",
    animelist_studio.studio_name AS "Studio Produksi",
    animelist_genreanime.genre AS "Genre Anime"
FROM animelist_anime
JOIN animelist_studio ON (animelist_studio.id = animelist_anime.studio_id)
JOIN animelist_genreanime ON (animelist_genreanime.id = animelist_anime.genre_id); -- query berhasil
