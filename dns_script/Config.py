#!/usr/bin/python3

import configparser

config_dir=""
config = configparser.ConfigParser()
config.read(config_dir)

#CoreDNS's Corefile directory
corefile_dir = config['path']['corefile']

#DNS forward address
dns = config['dns']['dns']

#MySQL Server Informations (Change before use)
ip = config['database']['ip']
username = config['database']['username']
password = config['database']['password']
dbName = config['database']['db']

