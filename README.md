Car Insurance Premium Simulator

## Description

The Car Insurance Premium Simulator is a backend service designed to calculate car insurance premiums based on key factors such as the car's age, value, deductible percentage, and a broker's fee. This service ensures that users receive an accurate and configurable insurance premium calculation.

The implementation follows best practices, including:

FastAPI for the backend framework

Docker for containerization

Domain-Driven Design (DDD), S.O.L.I.D., and Clean Architecture principles

### Project's Folder Setup
In the Entities folder, the Car and Policy entities are placed because they can change over time and have a unique identity.

In the value_objects folder, immutable objects that do not have a unique identification and are part of an action are inserted.

In the aggregate folder, entities that function as a single entity are grouped together to ensure consistency rules. In this case, the premium calculation uses entities and value objects, which are aggregated to produce a single output.

In the services folder, services that implement business rules that do not belong to a single entity are placed. These services typically use multiple external and internal services and are called by endpoints to execute business logic.

### Running the Project
To run the project, you need to have Docker and docker-compose installed on your machine.

You can use the commands in the Makefile:

make up → to start the installation and configuration of the containers.
make down → to stop the containers.
Once the setup is complete, the application will be running on port 8000.

To access the premium calculation route, you can use Postman or cURL, as shown in the example below:


curl --location 'http://127.0.0.1:8000/calculate-premium' \
--header 'Content-Type: application/json' \
--data '{
  "make": "Toyota",
  "model": "Corolla",
  "year": 2021,
  "value": 120000.0,
  "deductible_percentage": 0.10,
  "broker_fee": 50.0,
  "registration_location": "New York"
}'

## Currently, environment variables are passed through the Dockerfile. In the future, they will be managed via Terraform or pipelines using GitHub Secrets for better security of the information.