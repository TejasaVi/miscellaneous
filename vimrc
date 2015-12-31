syntax enable
set tabstop=4
set softtabstop=4
set expandtab
set shiftwidth=4
set ruler
set textwidth=79
set autoindent
set fileformat=unix

set nonu
set showcmd
set colorcolumn=80
set cursorline
filetype indent on
set paste

set wildmenu	"visual autocomplete for command menu
set showmatch 	 "highlights matching [{()}]

"Searching
set incsearch
set hlsearch
:highlight ExtraWhitespace ctermbg=red guibg=red
:match ExtraWhitespace /\s\+$/
