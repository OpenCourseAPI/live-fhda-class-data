import sys, json;

filepath = sys.argv[1]

f = open(filepath, "r")
beautified = json.dumps(json.load(f), indent=2)

f = open(filepath, "w")
f.write(beautified)
f.close()
