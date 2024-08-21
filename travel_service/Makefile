.PHONY: generate_migration
generate_migration:
	poetry run alembic revision --autogenerate -m "$(NAME)"

.PHONY: migrate
migrate:
	poetry run alembic upgrade head
