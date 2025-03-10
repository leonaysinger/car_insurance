# Define variables
DOCKER_COMPOSE = docker-compose
DOCKER_COMPOSE_FILE = docker-compose.yml

# Build and start the services
up:
	@echo "Starting Docker Compose services..."
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) up --build -d
	@echo "Services are running in the background."

# Stop and remove the services
down:
	@echo "Stopping and removing Docker Compose services..."
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down
	@echo "Services have been stopped and removed."

# View logs from the containers
logs:
	@echo "Displaying logs from Docker Compose services..."
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) logs -f

# Restart the services
restart:
	@echo "Restarting Docker Compose services..."
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) up -d
	@echo "Services have been restarted."

# Remove all Docker volumes (this will remove persistent data)
volumes:
	@echo "Removing Docker volumes..."
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down -v
	@echo "Docker volumes have been removed."

# Build Docker images (without starting containers)
build:
	@echo "Building Docker images..."
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) build
	@echo "Docker images have been built."

# Show running services
ps:
	@echo "Showing running Docker Compose services..."
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) ps

test-coverage:
	pytest --cov=app --cov-report=term --cov-report=html
