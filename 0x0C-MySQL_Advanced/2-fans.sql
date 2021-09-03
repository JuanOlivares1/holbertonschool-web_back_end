-- Sums number of fans by country
SELECT m.origin, SUM(m.fans) AS nb_fans
FROM metal_bands m
GROUP BY m.origin
ORDER BY nb_fans DESC;