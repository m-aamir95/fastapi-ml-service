#!/bin/bash

# Getting the public IP of the system, it will be injected via env variables in the reactjs frontend
# So that it can access backend hosted on the right server
env_file=.frontend_env_variales.env
touch $env_file
public_ip=$(curl -s ifconfig.me/ip)
echo "public_ip=$public_ip" >> $env_file