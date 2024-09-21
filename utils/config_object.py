import configparser

config = configparser.ConfigParser()
config.read("/config.txt")

WIDTH = config.get('default', 'WIDTH')
HEIGHT = config.get('default', 'HEIGHT')
FPS = config.get('default', 'FPS')

BLACK = config.get('default', 'BLACK').split(',')
WHITE = config.get('default', 'WHITE').split(',')
RED = config.get('default', 'RED').split(',')

PARTICLE_SIZE = config.get('default', 'PARTICLE_SIZE')
BLACKHOLE_SIZE = config.get('default', 'BLACKHOLE_SIZE')

GRAVITATION_CONSTANT = config.get('default', 'GRAVITATION_CONSTANT')
FIELD_VARIATION = config.get('default', 'FIELD_VARIATION')
TANGENTIAL_FACTOR = config.get('default', 'TANGENTIAL_FACTOR')
MAX_VELOCITY = config.get('default', 'MAX_VELOCITY')

PARTICLE_DENSITY = config.get('default', 'PARTICLE_DENSITY')

COLOR_VARIATION = config.get('default', 'COLOR_VARIATION')