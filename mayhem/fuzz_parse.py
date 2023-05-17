#!/usr/bin/python3
import json
import atheris
import sys

with atheris.instrument_imports():
    from jsonrpcclient import parse

def RandomString(fdp, min_len, max_len):
    str_len = fdp.ConsumeIntInRange(min_len, max_len)
    return fdp.ConsumeUnicodeNoSurrogates(str_len)

def StringDict(feed_str):
    try:
        return json.loads(feed_str)
    except:
        return {}

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    json_str = RandomString(fdp, 0, 1000)
    json_dict = StringDict(json_str)

    try:
        parse(json_dict)
    except KeyError:
        pass
    except TypeError:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()