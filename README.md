## Description
This repository contains a chat service that utilizes a Qwen 2.5 3B Instruct model to answer queries. 

## Setup

### Run docker container
```
cd build
docker compose up 
```

## Endpoints
/answer : Answers query from user input 

## Directory Tree
```
├── build
│   ├── .env
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── requirements.txt
├── README.md
├── src
│   ├── main.py
│   └── model.py
└── test
    ├── test_endpoint.py
    └── test_model.py
```