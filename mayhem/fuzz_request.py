#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from jsonrpcclient import request

def RandomString(fdp, min_len, max_len):
  str_len = fdp.ConsumeIntInRange(min_len, max_len)
  return fdp.ConsumeUnicodeNoSurrogates(str_len)

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    request_str = RandomString(fdp, 0, 128)

    request(request_str)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()