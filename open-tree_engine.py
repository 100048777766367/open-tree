import os, json, subprocess
TARGET_REPO = os.environ.get("TARGET_REPO", "retina")
SHARED_DIR = "/tmp/bodhi_workspace"
os.makedirs(SHARED_DIR, exist_ok=True)
os.chdir(SHARED_DIR)

print(f"🌲 [OPEN-TREE] Bắt đầu quét kiến trúc Read-Only cho {TARGET_REPO}...")
if not os.path.exists(TARGET_REPO):
    subprocess.run(["git", "clone", "--depth", "1", f"https://github.com/100048777766367/{TARGET_REPO}.git"])

tree_data = {"repo": TARGET_REPO, "all_paths": []}
for root, dirs, files in os.walk(TARGET_REPO):
    if ".git" in root: continue
    for d in dirs: tree_data["all_paths"].append(os.path.relpath(os.path.join(root, d), TARGET_REPO))
    for f in files: tree_data["all_paths"].append(os.path.relpath(os.path.join(root, f), TARGET_REPO))

with open("tree_data.json", "w") as f: json.dump(tree_data, f)
print("✅ [OPEN-TREE] Đã chụp X-Quang xong, cất vào bộ nhớ tạm.")
