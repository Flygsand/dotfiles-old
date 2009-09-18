#!/bin/sh

__gnome_init() {
  gnome-screensaver &
  gnome-settings-daemon &
  gnome-volume-manager &  
}

case $1 in
awesome)
	__gnome_init
	exec awesome
	;;

dwm)	
	__gnome_init
	exec dwm
	;;

gnome)
	exec gnome-session
	;;

i3)	
	__gnome_init
	exec i3
	;;

wmii)	
	__gnome_init
	exec wmii
	;;
*)
	__gnome_init
	exec wmii
	;;
esac
