import re

m = re.match("/(.*)/(.*)/(.*)", "/usr/home/hill")
print(m.groups())
