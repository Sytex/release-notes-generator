#!/usr/bin/env bash

set -eo pipefail

pull_request_number=${{ github.event.number }}

echo "Pull Request Number: $pull_request_number"
data=$(gh pr view $pull_request_number)
echo $data | python src/main.py

