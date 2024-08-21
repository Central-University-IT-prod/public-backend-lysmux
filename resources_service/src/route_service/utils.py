import math


def lat_to_y(lat: float, zoom: int) -> int:
    step = math.log(math.tan(lat * math.pi / 180) + 1 /
                    math.cos(lat * math.pi / 180))
    return (1 - step / math.pi) / 2 * pow(2, zoom)


def lon_to_x(lon: float, zoom: int) -> int:
    return ((lon + 180) / 360) * pow(2, zoom)
