#!/bin/bash

curl "http://localhost:8000/cards/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
