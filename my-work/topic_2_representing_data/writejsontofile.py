# playing with json
# Author: Tihana Gray

from pathlib import Path
import json

data = {
    "name": "joe",
    "age": 21,
    "student": True
}

# Path to silly.json to be beside this script
out_path = Path(__file__).parent / "silly.json"

with out_path.open("w") as fp:
    json.dump(data, fp, indent=4)

jsonString = json.dumps(data)
print("Wrote:", out_path)
print(data)
print(jsonString)