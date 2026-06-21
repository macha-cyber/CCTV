#!/bin/bash

cd /workspace

if [ -d apps/web ]; then
  cd apps/web
  npm install
fi

if [ -f apps/api/requirements.txt ]; then
  pip install -r apps/api/requirements.txt
fi

if [ -f apps/detector/requirements.txt ]; then
  pip install -r apps/detector/requirements.txt
fi