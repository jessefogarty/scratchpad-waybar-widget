#!/bin/bash
mapfile -t scratchpads < <(python3 /home/unkwn1/gits/scratchpad-waybar-widget/scratchpads.py)
choice=$(gum choose "${scratchpads[@]}")
swaymsg "[title=\"${choice}\"] scratchpad show"