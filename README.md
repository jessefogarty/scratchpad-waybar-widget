# scratchpad-waybar-widget
A widget to display the number of active scratchpads in a wayland session.

## Dependancies

Most will be preinstalled with any OS.

  - `gum` - available via most package managers (apt, pacman, duf, apk, pkg)

## Installation

### Automated Install

Coming soon...

### Manual Install

`git clone https://github.com/jessefogarty/scratchpad-waybar-widget.git && cd scratchpad-waybar-widget`

`cp scratchpad.py tui.sh ~/.config/waybar/scripts/`

Add the following to your waybar config file:

> :memo: NOTE - For the `on-click` exec I suggest adding the fullpath instead of the relative `~/`

```
// scratchpads
    "custom/scratchpads": {
        "interval": 2,
        "exec": "python3 ~/.config/waybar/scripts/scratchpads.py --waybar",
        "format": "{}",
        "on-click": "kitty sh '~/.config/waybar/scratchpad-waybar-widget/tui.sh'"
    },
```


## TODO

  - [ ] branch for wofi instead of gum (gum a better non wayland dependant)
