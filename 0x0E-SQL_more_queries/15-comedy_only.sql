-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_shows.title FROM tv_shows
JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
