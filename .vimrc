set nocompatible
syntax on
filetype on
filetype indent on
filetype plugin on
set cindent
set smartindent
set autoindent
set expandtab
set tabstop=2
set shiftwidth=2
set number
set wildmode=longest,list
set cursorline
vmap <Tab> >gv
vmap <S-Tab> <gv
map <C-G> :BufExplorer<CR>
map <C-F> :FSHere<CR>
set t_Co=256
colorscheme wombat256
