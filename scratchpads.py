import json
import subprocess
import sys
from argparse import ArgumentParser

KEYS = ["id", "pid", "name", "app_id", "visible", "sticky", "shell", "marks", "focused", "inhibit_idle"]
ICON = u"\uFBB6"
TUI = "./tui.sh"
def generate_tree():
    _data = subprocess.run(["swaymsg", "-t", "get_tree"], stdout=subprocess.PIPE).stdout.decode("utf-8")
    data = json.loads(_data)
    try:
        return data["nodes"][0]["nodes"][0]["floating_nodes"]
    except:
        return

def find_scratchpads2(waybar=False):
    try:
        root = generate_tree()
    except:
        return (0, [])
    node_filter = lambda _node: {k: _node[k] for k in KEYS}
    scratchpads = [node_filter(node)for node in root]
    if waybar == True:
        return f"{ICON} {len(scratchpads)}\n{ICON} Active number of scratchpads"
    else:
        windows = "\n".join([f"{node['name']}" for node in scratchpads]).strip()

        sys.stdout.write(windows)
        #return 

def focus_scratchpad(name):
    subprocess.run(["swaymsg", f"[title=\"{name}\"] focus"])

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--waybar", action="store_true", default=False)
    args = parser.parse_args()
    if args.waybar:
        print(find_scratchpads2(waybar=True))
    else:
        find_scratchpads2()
