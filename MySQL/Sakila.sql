SELECT city.city_id, city.city, customer.first_name, customer.last_name, customer.email, address.address
FROM city
LEFT JOIN address on city.city_id = address.city_id
LEFT JOIN customer on customer.address_id = address.address_id
WHERE city.city_id = 312;

SELECT film.film_id, film.title AS title, film.description AS description, 
film.release_year AS release_year, film.rating AS rating, film.special_features AS special_features, category.name AS genre
FROM film
LEFT JOIN film_category ON film.film_id = film_category.film_id
LEFT JOIN category ON film_category.category_id = category.category_id
WHERE category.name = "Comedy";

SELECT film_actor.actor_id, CONCAT(actor.first_name, " ", actor.last_name) AS actor_name,  
film_actor.film_id, film.title, film.description, film.release_year
FROM film_actor
LEFT JOIN film ON film_actor.film_id = film.film_id
LEFT JOIN actor on film_actor.actor_id = actor.actor_id
WHERE film_actor.actor_id = 5;

SELECT customer.store_id, city.city_id, customer.first_name, customer.last_name, customer.email, address.address
FROM customer
LEFT JOIN address ON customer.address_id = address.address_id
LEFT JOIN city ON address.city_id = city.city_id
WHERE customer.store_id = 1 
	AND city.city_id = 1
    OR city.city_id = 42
    OR city.city_id = 312
    OR city.city_id = 459;
    
SELECT film.title AS title, film.description AS description, 
film.release_year AS release_year, film.rating AS rating, film.special_features AS special_features
FROM film
LEFT JOIN film_category ON film.film_id = film_category.film_id
LEFT JOIN category ON film_category.category_id = category.category_id
LEFT JOIN film_actor ON film.film_id = film_actor.film_id
WHERE film_actor.actor_id = 15
AND rating = "G"
AND special_features LIKE "%Behind the Scenes%";

SELECT film.film_id, film.title AS title, actor.actor_id, CONCAT(actor.first_name, " ", actor.last_name) AS actor_name
FROM film
LEFT JOIN film_actor ON film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

SELECT film.film_id, film.title AS title, film.description AS description, 
film.release_year AS release_year, film.rating AS rating, film.special_features AS special_features, category.name AS genre,
film.rental_rate
FROM film
LEFT JOIN film_category ON film.film_id = film_category.film_id
LEFT JOIN category ON film_category.category_id = category.category_id
WHERE category.name = "Drama"
AND film.rental_rate = 2.99;

SELECT film_actor.actor_id, CONCAT(actor.first_name, " ", actor.last_name) AS actor_name,  
film_actor.film_id, film.title, film.description, film.release_year, film.rating AS rating, film.special_features AS special_features,
category.name AS genre
FROM film_actor
LEFT JOIN film ON film_actor.film_id = film.film_id
LEFT JOIN actor on film_actor.actor_id = actor.actor_id
LEFT JOIN film_category ON film.film_id = film_category.film_id
LEFT JOIN category ON film_category.category_id = category.category_id
WHERE CONCAT(actor.first_name, " ", actor.last_name) = "SANDRA KILMER"
AND  category.name = "Action";