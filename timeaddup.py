#!/usr/bin/env python3

import sys
import timecalc

result = timecalc.calc(sys.argv[1])

result = result.replace(".", ",")

print(result)