#!/bin/bash

source ./assets/argparse.sh

define_arg "skip_wandb" "false" "Whether to skip cleaning wandb" "boolean" "optional"
define_arg "skip_log" "false" "Whether to skip cleaning log" "boolean" "optional"

parse_args "$@"

if [ "$skip_log" = false ]; then
  rm -rf log
fi

if [ "$skip_wandb" = false ]; then
  rm -rf wandb
fi

rm -rf .ruff_cache
rm -rf .hypothesis
rm -rf .pytest_cache
rm -rf .vscode
rm -rf .idea
rm -rf .DS_Store
rm -rf .env
rm -rf .env.local
rm -rf .env.development.local
rm -rf .env.test.local
rm -rf .env.production.local
