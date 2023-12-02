#!/usr/bin/env bash

. .env

DAY=$1

curl "https://adventofcode.com/2023/day/$DAY/input" -X GET -H "Cookie: session=$SESSION"
