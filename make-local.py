#!/usr/bin/python

import sys
import os
import yaml
from jinja2 import Environment, FileSystemLoader

var_file = 'default_repo.yaml'

if len(sys.argv) >= 2:
  var_file = sys.argv[1]

data = {}
with open(var_file) as f:
  data = yaml.load(f)

#print "Data: "+str(data)
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('local-templ')
tokens = {'tokens': data }
mydict = data[0]
content = template.render(*data)
#content = template.render(**tokens)
with open("local.conf", "w") as f:
  f.write(content)


