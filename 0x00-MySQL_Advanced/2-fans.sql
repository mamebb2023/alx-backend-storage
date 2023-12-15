-- Group the fans by origins
SELECT
	origin, SUM(fans) AS nb_fans
	GROUP BY origin
	ORDER BY SUM(fans) DESC;
