#!/usr/bin/python3

import sys
import yaml
import pprint

pprint.pprint(yaml.load(open(sys.argv[1]).read(), Loader=yaml.FullLoader))
