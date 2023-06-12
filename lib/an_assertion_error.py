#!/usr/bin/env python3
try:
    assert 1 == 2, "Invalid Operation"

except AssertionError as msg:
    print(msg)
