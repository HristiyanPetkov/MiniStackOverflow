# MiniStackOverflow

This is a microservice-based application inspired by Stack Overflow, designed to demonstrate a full-fledged, scalable architecture using modern technologies. Below you'll find a comprehensive guide to understanding, setting up, and contributing to the project.

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
  - [Kubernetes](#kubernetes)

## Project Overview

MiniStackOverflow is a Q&A platform where users can post questions, provide answers, and comment on them. It leverages a microservice architecture to ensure scalability and maintainability, and it is fully deployed using Kubernetes for orchestration.

## Architecture

The application consists of several microservices, each responsible for a specific domain within the application. These services communicate via REST APIs and asynchronous messaging using Kafka.

- **Backend**: Developed with Java and Spring Boot
  - Authentication/User Service
  - Question Service
  - Answer Service
  - Comment Service
  - Notification Service
- **Frontend**: Developed with React
- **Communication**: Kafka for event-driven messaging
- **Caching**: Redis for caching frequently accessed data
- **Deployment**: Full deployment on Kubernetes

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: React
- **Messaging**: Kafka
- **Caching**: Redis
- **Deployment**: Kubernetes, Docker
- **Database**: MySQL


## Deployment

### Deploy to Kubernetes:

- Ensure your Kubernetes cluster is running
_ Apply the following files so that the needed environment is set up:
```bask
kubectl apply -f database-configMap.yaml
kubectl apply -f kafka-deployment.yaml
kubectl apply -f mysql-deployment.yaml
kubectl apply -f persistent-volume.yaml
kubectl apply -f redis-deployment.yaml
kubectl apply -f secrets.yaml
```
- Deploy the application services
```bash
cd ../Kubernetes
kubectl apply -f .
```
