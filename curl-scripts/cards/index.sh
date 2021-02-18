#!/bin/bash

curl "http://localhost:8000/cards/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
