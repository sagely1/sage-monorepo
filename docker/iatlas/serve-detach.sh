#!/usr/bin/env bash

product_name="iatlas"

args=(
  # List of services in alphanumeric order
  --file docker/"$product_name"/services/api.yml
  --file docker/"$product_name"/services/data.yml
  --file docker/"$product_name"/services/postgres.yml

  --file docker/"$product_name"/networks.yml
  --file docker/"$product_name"/volumes.yml

  --project-name "$product_name"

  up $1 --detach
)

docker compose "${args[@]}"
