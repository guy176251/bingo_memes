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
badd +22 README.md
badd +157 backend/backend/settings.py
badd +1 .env.old
badd +12 docker-compose.yml
badd +37 Dockerfile
badd +12 docker/prestart.sh
badd +0 backend/api/management/commands/init_db.py
argglobal
%argdel
tabnew +setlocal\ bufhidden=wipe
tabrewind
edit Dockerfile
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd _ | wincmd |
vsplit
1wincmd h
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
exe '1resize ' . ((&lines * 37 + 39) / 79)
exe 'vert 1resize ' . ((&columns * 71 + 71) / 142)
exe '2resize ' . ((&lines * 37 + 39) / 79)
exe 'vert 2resize ' . ((&columns * 70 + 71) / 142)
exe '3resize ' . ((&lines * 38 + 39) / 79)
argglobal
balt docker-compose.yml
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 37 - ((20 * winheight(0) + 18) / 37)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 37
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify(".env.old", ":p")) | buffer .env.old | else | edit .env.old | endif
if &buftype ==# 'terminal'
  silent file .env.old
endif
balt docker-compose.yml
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 18) / 37)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
lcd ~/code/django/bingo_memes
wincmd w
argglobal
if bufexists(fnamemodify("~/code/django/bingo_memes/backend/backend/settings.py", ":p")) | buffer ~/code/django/bingo_memes/backend/backend/settings.py | else | edit ~/code/django/bingo_memes/backend/backend/settings.py | endif
if &buftype ==# 'terminal'
  silent file ~/code/django/bingo_memes/backend/backend/settings.py
endif
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
155
normal! zo
let s:l = 157 - ((18 * winheight(0) + 19) / 38)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 157
normal! 020|
wincmd w
exe '1resize ' . ((&lines * 37 + 39) / 79)
exe 'vert 1resize ' . ((&columns * 71 + 71) / 142)
exe '2resize ' . ((&lines * 37 + 39) / 79)
exe 'vert 2resize ' . ((&columns * 70 + 71) / 142)
exe '3resize ' . ((&lines * 38 + 39) / 79)
tabnext
edit ~/code/django/bingo_memes/backend/api/management/commands/init_db.py
argglobal
balt ~/code/django/bingo_memes/docker/prestart.sh
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 38) / 76)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
lcd ~/code/django/bingo_memes
tabnext 2
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOF
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
nohlsearch
let g:this_session = v:this_session
let g:this_obsession = v:this_session
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
