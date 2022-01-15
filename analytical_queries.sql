-- Retrieve TOP 100 properties by their occupancy days and ranking them by that measure

SELECT *
FROM (
	SELECT s.property_id
		,date_part('month', s.start_date) AS Months
		,count(s.property_id)
		,sum(s.end_date - s.start_date) AS occupied
		,RANK() OVER (
			ORDER BY sum(s.end_date - s.start_date) DESC
			) AS property_rank
	FROM PUBLIC.stay s
	GROUP BY s.property_id
		,date_part('month', s.start_date)
	ORDER BY s.property_id
	) q
ORDER BY q.occupied DESC LIMIT 100

-- Retrieve properties that are the lowest (Bottom 100) logged but highest (Top 100) at occupancy

(
		SELECT l.property_id
		FROM logs l
		GROUP BY l.property_id
		ORDER BY count(log_id) ASC LIMIT 100
		)

INTERSECT

(
	SELECT q.property_id
	FROM (
		SELECT s.property_id
			,date_part('month', s.start_date) AS Months
			,count(s.property_id)
			,sum(s.end_date - s.start_date) AS occupied
		FROM PUBLIC.stay s
		GROUP BY s.property_id
			,date_part('month', s.start_date)
		ORDER BY s.property_id
		) q
	ORDER BY q.occupied DESC LIMIT 100
	)

    
-- Retrieve top 5 properties by price in each city

SELECT *
FROM (
	SELECT c.city
		,p.property_id
		,p.rent
		,RANK() OVER (
			PARTITION BY c.city ORDER BY p.rent DESC
			) AS ranking
	FROM properties p
	LEFT JOIN city c ON c.city_id = p.city_id
	) a
WHERE ranking <= 5
ORDER BY city
	,ranking
