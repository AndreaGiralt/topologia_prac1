.DEFAULT_GOAL := help
.PHONY: local dump start stop remove help console spider zones previews details csv

local:
	docker-compose up -d

console:
	docker-compose exec python_uoc bash

spider:
	docker-compose exec -w "/usr/src/app" python_uoc ./parser -a

zones:
	docker-compose exec -w "/usr/src/app" python_uoc ./parser -z

previews:
	docker-compose exec -w "/usr/src/app" python_uoc ./parser -p

details:
	docker-compose exec -w "/usr/src/app" python_uoc ./parser -d

csv:
	docker-compose exec -w "/usr/src/app" python_uoc ./parser -c

dump:
	docker-compose exec -w "/" mongo_uoc mongodump -d uoc --collection real_states
	docker-compose exec -w "/" mongo_uoc mongodump -d uoc --collection unemployment

start:
	docker-compose start

stop:
	docker-compose stop

remove:
	docker-compose down

help:
	@echo "🚀 local : build and launch local environment"
	@echo "🚀 console : open a python console"
	@echo "🚀 spider: runs the complete spider"
	@echo "🚀 zones: runs zones spider"
	@echo "🚀 previews: runs previews spider"
	@echo "🚀 details: runs details spider"
	@echo "🗂️ csv: dump into csv"
	@echo "🗂️ dump : dump database"
	@echo "🏁 start : starts environment"
	@echo "🛑 stop : stops environment"
	@echo "🗑️ remove : remove all containers"

