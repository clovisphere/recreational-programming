from itertools import chain
from typing import Any


class Helper:
    @classmethod
    def extract_key_value(cls, line: str) -> tuple[str, Any]:
        # what we consider to be valid 'bool' 😊
        booleans = { 'truthy': ['true', 'yes', 'on'], 'falsy': ['false', 'no', 'off'] }
        key, value = line.split('=')
        pair = cls.is_number_or_none(value)
        if pair[0]:
            value = pair[1]
        elif value.lower() in set(chain(*booleans.values())):
            value = False if value.lower() in booleans['falsy'] else True
        return key, value

    @staticmethod
    def is_number_or_none(s: str) -> list[bool|Any]:
        result = [False, None]
        try:
            number = float(s) if '.' in s else int(s)
            result[0], result[1] = True, number
        except ValueError:
            pass
        return result


def parse_config(path: str) -> dict[Any, Any]:
    with (file := open(path)):  # same as -> `with open(path) as file:`
        config, section = {}, None
        for line in (line.strip() for line in file if line.strip()):
            if line.startswith(';'): continue
            elif line.startswith('[') and line.endswith(']'):
                section = line.replace('[', '').replace(']', '').strip()
                config[section] = {}
            elif line.count('=') == 1:
                key, value = Helper.extract_key_value(line)
                config[section].update({key: value})
        return config
