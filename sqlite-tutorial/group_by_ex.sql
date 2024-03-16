-- Columns are albumid and count of number of trackids grouped by each albumid, and sorted with the greatest count at the top
SELECT
	albumid,
	COUNT(trackid)
FROM
	tracks
GROUP BY
	albumid
ORDER BY COUNT(trackid) DESC;