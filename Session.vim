let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/code/django/bingo_memes
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +4 .env.local
badd +1 README.md
badd +3 docker-compose.local.yml
badd +148 backend/backend/settings.py
argglobal
%argdel
edit .env.local
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
2wincmd h
wincmd w
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 94 + 142) / 284)
exe 'vert 2resize ' . ((&columns * 94 + 142) / 284)
exe 'vert 3resize ' . ((&columns * 94 + 142) / 284)
argglobal
balt backend/backend/settings.py
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 4 - ((3 * winheight(0) + 38) / 76)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 4
normal! 014|
lcd ~/code/django/bingo_memes
wincmd w
argglobal
if bufexists(fnamemodify("~/code/django/bingo_memes/backend/backend/settings.py", ":p")) | buffer ~/code/django/bingo_memes/backend/backend/settings.py | else | edit ~/code/django/bingo_memes/backend/backend/settings.py | endif
if &buftype ==# 'terminal'
  silent file ~/code/django/bingo_memes/backend/backend/settings.py
endif
balt ~/code/django/bingo_memes/.env.local
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 148 - ((42 * winheight(0) + 38) / 76)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 148
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("~/code/django/bingo_memes/README.md", ":p")) | buffer ~/code/django/bingo_memes/README.md | else | edit ~/code/django/bingo_memes/README.md | endif
if &buftype ==# 'terminal'
  silent file ~/code/django/bingo_memes/README.md
endif
balt ~/code/django/bingo_memes/.env.local
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 22 - ((21 * winheight(0) + 38) / 76)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 22
normal! 029|
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 94 + 142) / 284)
exe 'vert 2resize ' . ((&columns * 94 + 142) / 284)
exe 'vert 3resize ' . ((&columns * 94 + 142) / 284)
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOF
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
let g:this_session = v:this_session
let g:this_obsession = v:this_session
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
