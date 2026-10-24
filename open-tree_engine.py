import os, json, subprocess

TARGET = os.environ.get("TARGET_REPO", "retina")
WORKSPACE = "/tmp/bodhi_dissector"
os.makedirs(WORKSPACE, exist_ok=True)
os.chdir(WORKSPACE)

print(f"🌲 [OPEN-TREE REAL ENGINE] Bắt đầu quét cây kiến trúc cho: {TARGET}")
if not os.path.exists(TARGET):
    subprocess.run(["git", "clone", "--depth", "1", f"https://github.com/100048777766367/{TARGET}.git"])

tree_result = {"repo": TARGET, "paths": []}
for root, dirs, files in os.walk(TARGET):
    if ".git" in root or "__pycache__" in root: continue
    for d in dirs: tree_result["paths"].append(os.path.relpath(os.path.join(root, d), TARGET))
    for f in files:
        if not f.endswith((".pyc", ".ipynb")):
            tree_result["paths"].append(os.path.relpath(os.path.join(root, f), TARGET))

with open("tree_out.json", "w") as f: json.dump(tree_result, f)
print(f"✅ [OPEN-TREE] Đã lập bản đồ {len(tree_result['paths'])} đối tượng vào `tree_out.json`.")
