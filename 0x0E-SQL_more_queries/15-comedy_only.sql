-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.title
FROM tv_shows
JOIN tv_shows_genres
ON tv_shows.id = tv_shows_genres.id
JOIN tv_genres
ON tv_genres.id = tv_show_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
