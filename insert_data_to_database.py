import yaml
from database_interface.data_inserting import insert_data
with open('config/database_config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

server = config['server']
database = config['name']
username = config['username']
password = config['password']

insert_data(server, database, username, password)