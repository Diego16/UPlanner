#!/usr/bin/env bash
if [[ $# -eq 0 ]]
  then
    mysql -h localhost -P 3306 -uuplanner_user -puplanner_db_pwd -e "drop database if exists uplanner; create database uplanner;"
    python manage.py migrate
fi