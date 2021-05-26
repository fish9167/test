# -*- encoding: utf-8 -*-
#

import json
import sys

file_path=sys.argv[1]
version=sys.argv[2]

print("change version: %s, file: %s" %(version, file_path))

print("json load")
with open(file_path, "r",encoding='utf-8') as f:
	data = json.load(f)

print("change version")
data["version"] = version

print("save file")
with open(file_path, "w") as f:
	json.dump(data, f, indent=4, ensure_ascii=False)
