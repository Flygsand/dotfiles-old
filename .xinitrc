#!/bin/sh

__gnome_init() {
  gnome-screensaver &
  gnome-settings-daemon &
  gnome-volume-manager &  
}

case $1 in
awesome)
	__gnome_init
	exec ssh-agent awesome
	;;

dwm)	
	__gnome_init
	exec ssh-agent dwm
	;;

gnome)
	exec gnome-session
	;;

i3)	
	__gnome_init
	exec ssh-agent i3
	;;

wmii)	
	__gnome_init
	exec ssh-agent wmii
	;;
*)
	__gnome_init
	exec ssh-agent wmii
	;;
esac
