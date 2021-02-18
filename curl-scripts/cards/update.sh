#!/bin/bash

curl "http://localhost:8000/mangos/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "card": {
      "notes": "'"${NOTES}"'",
      "status": "'"${STATUS}"'",
    }
  }'

echo
