# Multi-Tier Web Application with Docker Compose

## Overview
This project is a multi-tier web application designed to showcase the integration of various services using Docker Compose. It includes components like Nginx, Flask application, Fluentd for logging, Elasticsearch for indexing, and Kibana for visualization.

## Project Structure
The Docker Compose file defines the following services:

- **fluentd:** Fluentd service for centralized logging.
- **nginx:** Nginx web server acting as a frontend.
- **flask_app:** Flask application serving as the backend.
- **elasticsearch:** Elasticsearch for indexing and storing logs.
- **kibana:** Kibana for visualizing logs stored in Elasticsearch.

## Tools Used
- **Docker:** Containerization of the application for consistency across different environments.
- **Docker Compose:** Defining and running multi-container Docker applications.
- **Fluentd:** Centralized logging tool.
- **Nginx:** Web server.
- **Flask:** Python web framework.
- **Elasticsearch:** Search and analytics engine.
- **Kibana:** Data visualization tool.

## Getting Started
Follow these steps to set up and run the multi-tier web application using Docker Compose.

### Prerequisites
- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

### Clone the Repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo

Build and Run

Use the following command to build and run the application:
docker-compose up -d

This command will start all the services defined in the Docker Compose file in detached mode.
Access the Application

Once the containers are up and running, you can access the application:

    Web App (Flask): http://localhost:5000
    Kibana: http://localhost:5601

Accessing Logs

Logs are centralized and can be viewed in Kibana. Access Kibana at http://localhost:5601 and set up your index patterns to explore logs.
Additional Commands

    To stop the application:

    docker-compose down

Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.
