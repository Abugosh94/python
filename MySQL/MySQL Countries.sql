SELECT name, languages.language, languages.percentage 
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE language="Slovene"
ORDER BY percentage DESC;

SELECT countries.name, count(*) as cities
FROM cities
LEFT JOIN countries 
ON cities.country_id = countries.id
GROUP BY countries.name
ORDER BY cities DESC;

SELECT name, population
FROM cities
WHERE population > 500000
AND country_id = 136
ORDER BY population DESC;

SELECT countries.name, languages.language, languages.percentage 
FROM languages
LEFT JOIN countries
ON country_id = countries.id
WHERE percentage > 89
ORDER BY percentage DESC;

SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501
AND population > 100000;

SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE government_form = "Constitutional Monarchy"
AND capital > 200
AND life_expectancy > 75;

SELECT countries.name AS "Country Name", cities.name AS "City Name", cities.district, cities.population
FROM cities
LEFT JOIN countries
ON country_id = countries.id
WHERE cities.population > 500000
AND country_id = 9
AND cities.district = "Buenos Aires"
ORDER BY population DESC;

SELECT region, count(*) as countries
FROM countries
GROUP BY region
ORDER BY countries DESC;