# -*- coding: utf-8 -*-

import re

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
res = re.sub(r'(\.|,)',"",str).split(" ")

print map(len, res)
