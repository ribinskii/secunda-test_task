.PHONY: up stop down rebuild clean ps

up:
	docker-compose up -d

stop:
	docker-compose stop

down:
	docker-compose down

rebuild:
	docker-compose up -d --build

clean:
	docker-compose down -v --rmi local

ps:
	docker-compose ps