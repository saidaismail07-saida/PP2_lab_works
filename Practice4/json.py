import json
# open and load JSON file
with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':6} {'MTU':6}")
print("-" * 80)

# loop through interfaces
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    
    dn = attributes["dn"]
    descr = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(f"{dn:50} {descr:20} {speed:6} {mtu:6}")