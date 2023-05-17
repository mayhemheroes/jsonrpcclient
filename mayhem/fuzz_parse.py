#!/usr/bin/python3
import atheris
import sys
from json import JSONDecodeError

with atheris.instrument_imports():
    from jsonrpcclient import parse_json

def RandomString(fdp, min_len, max_len):
    str_len = fdp.ConsumeIntInRange(min_len, max_len)
    return fdp.ConsumeUnicodeNoSurrogates(str_len)

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    json_str = RandomString(fdp, 0, 128)

    try:
        parse_json(json_str)
    except KeyError:
        pass
    except TypeError:
        pass
    except JSONDecodeError:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()