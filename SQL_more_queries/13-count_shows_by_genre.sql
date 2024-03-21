-- script that lists all genres from hbtn_0d_tvshows and displays the number
SELECT `tv_genres`.`name` AS `genre`,
    COUNT(*)  AS `number_of_shows`
  FROM `tv_genres`
       INNER JOIN `tv_show_genres` AS t
       ON `tv_genres`.`id` = t.`genre_id`
 GROUP BY `tv_genres`.`name`
 ORDER BY `number_of_shows` DESC;
