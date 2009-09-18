# Load modules
autoload colors zsh/terminfo
if [[ "$terminfo[colors]" -ge 8 ]]; then
  colors
fi

# Set prompt
export PS1="%{%(#.$fg_bold[red].$fg_bold[green])%}%m %{$fg_bold[blue]%}%~%#%{$reset_color%} "
export EDITOR=vim

# Safety precautions
alias 'rm=rm -i'
alias 'mv=mv -i'
alias 'cp=cp -i'

# For convenience
alias 'mkdir=mkdir -p'
alias 'nano=nano -w'
alias 'blinkenshell=ssh -p 2222 mtah@titan.blinkenshell.org'
alias 'eris=ssh hager@eris.ctk.se'
alias 'chalmers=ssh hager@remote3.studat.chalmers.se'
alias 'mountrepo=sshfs -p 2222 -o follow_symlinks -o uid=`id -u` -o gid=`id -g` mtah@titan.blinkenshell.org:./public_html/repo'
alias 'cleanmakepkg=LC_ALL=C makepkg --config /etc/makepkg.clean.conf'

# Typing errors
alias 'cd..=cd ..'

# Coloured output
alias 'ls=ls --color=auto'
alias 'grep=grep --colour=auto'

# Prevent nautilus from managing the desktop
# if we're outside of GNOME
if [[ -z `pidof /usr/bin/gnome-session` ]]; then
  alias 'nautilus=nautilus --no-desktop'
fi

# Set window title on X terminals
__change_window_title () { 
  echo -en "\033]0;$(print -P "%n@%m:%~")\007";
}

case $TERM in
  xterm*|screen*|rxvt*)
    precmd () { __change_window_title; }
    chpwd () { __change_window_title; }
    ;;
  *)
    ;;
esac

