#!/bin/bash

curl "http://localhost:8000/cards/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "card": {
      "notes": "'"${NOTES}"'",
      "status": "'"${STATUS}"'"
    }
  }'

echo
