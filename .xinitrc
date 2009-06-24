export OOO_FORCE_DESKTOP=gnome
xrdb -merge /home/mtah/.Xresources

# .Xmodmap remaps Caps Lock to Esc (for Vim)
if [ -f /home/mtah/.Xmodmap ]; then
  xmodmap /home/mtah/.Xmodmap
fi

firefox&
piding&
gvim&
urxvt&

env WINEPREFIX="/home/mtah/.wine" wine "C:\Program Files\Spotify\spotify.exe"&

dbus-launch --sh-syntax --exit-with-session /usr/bin/xmonad
