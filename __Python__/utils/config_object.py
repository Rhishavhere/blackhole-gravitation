import configparser
import ast

config = configparser.ConfigParser()
config.read("/config.txt")

def parse_value(value):
  try:
    return ast.literal_eval(value)
  except (ValueError, SyntaxError):
    return value

WIDTH = parse_value(config.get('DEFAULT', 'WIDTH'))
HEIGHT = parse_value(config.get('DEFAULT', 'HEIGHT'))
FPS = parse_value(config.get('DEFAULT', 'FPS'))

BLACK = parse_value(config.get('DEFAULT', 'BLACK'))
WHITE = parse_value(config.get('DEFAULT', 'WHITE'))
RED = parse_value(config.get('DEFAULT', 'RED'))

PARTICLE_SIZE = parse_value(config.get('DEFAULT', 'PARTICLE_SIZE'))
BLACKHOLE_SIZE = parse_value(config.get('DEFAULT', 'BLACKHOLE_SIZE'))

GRAVITATION_CONSTANT = parse_value(config.get('DEFAULT', 'GRAVITATION_CONSTANT'))
FIELD_VARIATION = parse_value(config.get('DEFAULT', 'FIELD_VARIATION'))
TANGENTIAL_FACTOR = parse_value(config.get('DEFAULT', 'TANGENTIAL_FACTOR'))
MAX_VELOCITY = parse_value(config.get('DEFAULT', 'MAX_VELOCITY'))

PARTICLE_DENSITY = parse_value(config.get('DEFAULT', 'PARTICLE_DENSITY'))

COLOR_VARIATION = parse_value(config.get('DEFAULT', 'COLOR_VARIATION'))


print(f"WIDTH: {WIDTH}, type: {type(WIDTH)}")