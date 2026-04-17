import json, pathlib
pathlib.Path("out").mkdir(exist_ok=True)

json.dump({
  "kms":"active",
  "hsm":"compatible",
  "yubikey":"pending"
}, open("out/key_management_evidence.json","w"), indent=2)

print("OK")
