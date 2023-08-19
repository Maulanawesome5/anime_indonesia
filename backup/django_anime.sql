-- Active: 1667427687682@@localhost@3306@django_anime

SELECT VERSION();
USE django_anime;
SHOW TABLES;

SELECT * FROM api_anime ORDER BY anime_title ASC;
SELECT * FROM api_anime ORDER BY LENGTH(anime_title) DESC;
DESCRIBE api_anime; DESCRIBE api_studio;

SELECT
    mal_id AS MAL_ID,
    anime_title AS TITLE,
    LENGTH(anime_title) AS LEN_JUDUL
FROM api_anime ORDER BY LENGTH(anime_title) DESC;

SELECT id, mal_id, anime_title, anime_score, api_url, post_url FROM api_anime;
SELECT * FROM api_studio ORDER BY studio_name ASC;