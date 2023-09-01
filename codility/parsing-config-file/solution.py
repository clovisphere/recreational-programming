from itertools import chain
from typing import Any


class Helper:
    @classmethod
    def extract_key_value(cls, line: str) -> tuple[str, Any]:
        # what we consider to be valid 'bool' 😊
        booleans = { 'truthy': ['true', 'yes', 'on'], 'falsy': ['false', 'no', 'off'] }
        key, value = line.split('=')
        if cls.is_number(value):
            value = float(value) if '.' in value else int(value)
        elif value.lower() in set(chain(*booleans.values())):
            value = False if value.lower() in booleans['falsy'] else True
        return key, value

    @staticmethod
    def is_number(s: str) -> bool:
        """Returns True if s is a valid int/float, False otherwise."""
        try:
            _ = float(s)
            return True
        except ValueError:
            return False


def parse_config(path: str) -> dict[Any, Any]:
    with (file := open(path)):  # same as -> `with open(path) as file:`
        config, section = {}, None
        for line in (line.strip() for line in file if line.strip()):
            if line.startswith(';'): continue
            elif line.startswith('[') and line.endswith(']'):
                section = line.replace('[', '', 1).replace(']', '', 1).strip()
                config[section] = {}
            elif line.count('=') == 1:
                key, value = Helper.extract_key_value(line)
                config[section].update({key: value})
        return config
