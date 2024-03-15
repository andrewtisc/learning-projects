-- Gets all tracks with unknown first character, then 'ere', then any number of characters after
SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name GLOB '?ere*';