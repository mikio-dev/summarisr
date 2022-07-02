#! /usr/bin/env bash

export APP_MODULE=${APP_MODULE-summarisr.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8001}

# run gunicorn
exec gunicorn --bind $HOST:$PORT "$APP_MODULE" -k uvicorn.workers.UvicornWorker