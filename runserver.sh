#! /bin/bash

run_server() {
    cd "$1"
    source ./venv/bin/activate
    uvicorn "$2" --reload --port "$3"
    deactivate
    cd ..
}

docker compose up -d

run_server "gateway" "app.main:app" 8000 &
run_server "projects" "app.main.main:app" 8001 &
run_server "user" "app.infra.main:app" 8002 &

wait
