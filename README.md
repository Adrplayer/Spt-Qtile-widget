# Spt-Qtile-widget
a qtile widget based on sp command for control spotify

Features:
 - Name and artist of the current song
 - control of song by mouse
## Controls
 - left click - play/pause
 - scroll up - next song
 - scroll down - previous song

## Related proyects
I was guided by the Cmus built-in widget and inspired from the [awesomewm-spotify-widget from streetturtle](https://github.com/streetturtle/awesome-wm-widgets/tree/master/spotify-widget).

## Instalation
the spotify CLI need to be installed, after that:

clone the repository and add spt.py to the widgets carpet on libqtile
(this carpet i found in /lib64/python3.9/site-packages/libqtile/widget/)
for the recognition of the new widget by qtile, is needed to add him to \__init__.py file

    #add this to your __init__.py (line 91)
    "Spt":"spt",
