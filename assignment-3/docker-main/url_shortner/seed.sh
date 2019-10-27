#!/usr/bin/env sh

# run this script after `flask db-init` to seed the database with sample data

curl -X "POST" --data url=https://www.github.com "http://127.0.0.1:5000/" > /dev/null
sleep 2
curl -X "POST" --data url=https://www.amazon.com "http://127.0.0.1:5000/" > /dev/null
sleep 2
curl -X "POST" --data url=https://www.google.com "http://127.0.0.1:5000/" > /dev/null
sleep 2
curl -X "POST" --data url=https://home.cern "http://127.0.0.1:5000/" > /dev/null
sleep 2
curl -X "POST" --data url=https://nl.burberry.com "http://127.0.0.1:5000/" > /dev/null
