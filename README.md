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