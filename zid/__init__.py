import os
import re

try:
    with open(".env") as file:
        content = file.read()
except IOError:
    content = ""

for line in content.splitlines():
    match = re.match(r"\A([A-Za-z_0-9]+)=(.*)\Z", line)

    if match:
        k, v = match.group(1), match.group(2)

        single = re.match(r"\A'(.*)'\Z", v)

        if single:
            v = single.group(1)

        double = re.match(r'\A"(.*)"\Z', v)

        if double:
            v = re.sub(r"\\(.)", r"\1", double.group(1))

        os.environ.setdefault(k, v)
