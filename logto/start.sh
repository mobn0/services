#!/bin/sh
set -e

npm run cli db seed -- --swe
npm start