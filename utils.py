from enum import Enum
import ctypes

class DamageType(Enum):
    EARTH = 'earth'
    WATER = 'water'
    AIR = 'air'
    FIRE = 'fire'

def get_screen_size():
    user32 = ctypes.windll.user32
    screenx = user32.GetSystemMetrics(0)
    screeny = user32.GetSystemMetrics(1)
    return screenx,screeny