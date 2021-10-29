.DEFAULT_GOAL := help
.PHONY: local image composer migrate database pgbadger start stop remove help

local: image
	docker volume create mongo-is
	docker volume create postgresql-is
	docker network create cms || true
	docker network create traefik || true
	docker-compose up -d

image:
	docker build -f apache/Dockerfile ../../ --tag ecommerce-is/apache:local
	docker build -f php/Dockerfile ../../ --tag ecommerce-is/php:local
	docker build -f scss/Dockerfile ../../ --tag ecommerce-is/scss:local
	docker build -f mongo/Dockerfile ../../ --tag ecommerce-is/mongo:local
	docker build -f postgresql/Dockerfile ../../ --tag ecommerce-is/postgresql:local
	docker build -f php/Dockerfile-cron ../../ --tag ecommerce-is/cron:local

composer:
	docker-compose exec php-is composer update --working-dir=/var/www/islas4/is/composer/iceland
	docker-compose exec php-is composer update --working-dir=/var/www/islas4/is/composer/iceland

migrate:
	docker-compose exec -w "/var/www/islas4/is/core_src/Scripts/migrations" php-is ./migrate.php islas4dev-is.deswebislas.com migrations:migrate

migration_generate:
	docker-compose exec -w "/var/www/islas4/is/core_src/Scripts/migrations" php-is ./migrate.php islas4dev-is.deswebislas.com migrations:generate

nav_items:
	docker-compose exec -w "/var/www/islas4/is/baltics_src/core_src/Scripts/Iceland/Navision" php-is ./importFullConcurrently.php islas4dev-is.deswebislas.com reimport

nav_prices:
	docker-compose exec -w "/var/www/islas4/is/baltics_src/core_src/Scripts/Iceland/Navision" php-is ./importFullConcurrently.php islas4dev-is.deswebislas.com update


database:
	docker-compose exec postgresql-is ash /docker-entrypoint-initdb.d/init_docker_postgres.sh

pgbadger:
	docker cp iceland_postgresql-is_1:/logs/postgresql.log .
	cat postgresql.log | docker run -i --rm matsuu/pgbadger --prefix='%t [%p]: [%l-1] db=%d,user=%u' - -o - -x html > report.html

start:
	docker-compose start

stop:
	docker-compose stop

remove:
	docker-compose down

help:
	@echo "🚀 local : build and launch local environment"
	@echo "🖼️ image : build local images"
	@echo "🎵 composer : install composer packages"
	@echo "🗂️ database : dump development database to local"
	@echo "🦡 pgbadger : create report from local PostgreSQL"
	@echo "🔁 nav_items : import the items from Navision"
	@echo "🔄 nav_prices : update the prices from Navision"
	@echo "♻ migrate : execute the project's migrations"
	@echo "🏁 start : starts environment"
	@echo "🛑 stop : stops environment"
	@echo "🗑️ remove : remove all containers"



#mongodump -d real_states --port 27999 --collection ids
#mongodump -d real_states --port 27999 --collection details