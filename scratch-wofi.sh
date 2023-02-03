#!/usr/bin/bash


select=$(python3 /home/unkwn1/gits/scratchpad-waybar-widget/scratchpads.py | wofi -d -W 20% --lines 5 2>/dev/null)
swaymsg "[title=$select] scratchpad show"
