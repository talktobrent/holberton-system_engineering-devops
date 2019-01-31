#!/usr/bin/env bash
# Dumps all mysql databases and compresses archive
set -e
mysqldump --all-databases --events -uroot -p"$1" > backup.sql
tar -czvf "$(date '+%d-%m-%Y').tar.gz" backup.sql
