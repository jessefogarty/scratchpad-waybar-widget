import json
import subprocess
import sys
from argparse import ArgumentParser

KEYS = ["id", "pid", "name", "app_id", "visible", "sticky", "shell", "marks", "focused", "inhibit_idle"]
ICON = u"\uFBB6"
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
    if waybar:
        return f"{ICON} {len(scratchpads)}\n{ICON} Active number of scratchpads"
    return (len(scratchpads), scratchpads)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--waybar", action="store_true", default=False)
    args = parser.parse_args()
    if args.waybar:
        print(find_scratchpads2(waybar=True))
    else:
        print(find_scratchpads2())
