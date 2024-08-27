# 0x03. Queuing System in JS

## Description
This project is focused on building a queuing system using Redis, NodeJS, ExpressJS, and Kue. You'll set up a Redis server, interact with it using Node.js, manage queues with Kue, and create a basic Express app that integrates with Redis.

## Learning Objectives
By the end of this project, you should be able to:
- Set up and run a Redis server.
- Perform basic Redis operations via the Redis client.
- Use Node.js to interact with Redis.
- Handle asynchronous operations in Redis.
- Implement queue management using Kue.
- Build a basic Express app that interacts with both Redis and Kue.

## Requirements
- **OS:** Ubuntu 18.04 LTS
- **Node.js:** v12.x
- **Redis:** v6.0.10 or higher
- **JavaScript Standard:** ES6
- **Linting:** ESLint
- **Package Manager:** npm

## Setup Instructions

### 1. Install Redis
Download, extract, and compile Redis 6.0.10:
```bash
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make

