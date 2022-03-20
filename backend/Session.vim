let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/code/django/bingo_memes/backend
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +453 card/models.py
badd +40 card/api.py
badd +158 card/tests.py
badd +69 card/factories.py
badd +20 user/models.py
badd +2 card/signals.py
badd +143 backend/settings.py
badd +5 test-server
badd +8 reset-db
badd +25 backend/urls.py
badd +15 card/schema.py
badd +24 core/management/commands/init_db.py
badd +7 card/exceptions.py
badd +86 conftest.py
badd +1 user/tests.py
badd +1 user/querysets.py
badd +10 user/api.py
badd +4 user/schema.py
badd +6 category/schema.py
badd +1 category/models.py
badd +14 user/factories.py
badd +1 .old/generics/management/commands/init_db.py
badd +1 category/factories.py
badd +1 category/tests_old.py
badd +1 ~/code/django/bingo_memes/docker-compose.yml
badd +31 ~/code/django/bingo_memes/Dockerfile
badd +2 ~/code/django/bingo_memes/docker/print-nginx-conf.sh
badd +22 ~/code/django/bingo_memes/docker/prestart.sh
badd +4 ~/code/django/bingo_memes/.env
badd +10 card/admin.py
badd +9 card/apps.py
badd +1 user/migrations/0001_initial.py
badd +10 user/signals.py
badd +9 user/apps.py
badd +1 pyproject.toml
badd +1 ~/code/django/simplyhired_scraper/pyproject.toml
badd +1 hashtag/models.py
badd +108 core/api.py
badd +7 card/models/names.py
badd +71 card/models/__init__.py
badd +73 card/models/base.py
badd +23 card/models/relations.py
badd +192 card/models/plumbing.py
badd +23 card/models/const.py
argglobal
%argdel
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabrewind
edit card/models/base.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
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
exe 'vert 1resize ' . ((&columns * 142 + 142) / 284)
exe 'vert 2resize ' . ((&columns * 141 + 142) / 284)
argglobal
balt card/tests.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 73 - ((71 * winheight(0) + 38) / 76)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 73
normal! 0
wincmd w
argglobal
if bufexists("card/models/plumbing.py") | buffer card/models/plumbing.py | else | edit card/models/plumbing.py | endif
if &buftype ==# 'terminal'
  silent file card/models/plumbing.py
endif
balt card/tests.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
20
normal! zo
44
normal! zo
49
normal! zo
66
normal! zo
78
normal! zo
116
normal! zo
120
normal! zo
121
normal! zo
133
normal! zo
138
normal! zo
140
normal! zo
175
normal! zo
184
normal! zo
185
normal! zo
let s:l = 14 - ((4 * winheight(0) + 38) / 76)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 14
normal! 016|
wincmd w
exe 'vert 1resize ' . ((&columns * 142 + 142) / 284)
exe 'vert 2resize ' . ((&columns * 141 + 142) / 284)
tabnext
edit ~/code/django/simplyhired_scraper/pyproject.toml
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
balt backend/settings.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 7 - ((6 * winheight(0) + 38) / 76)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 7
normal! 0
lcd ~/code/django/bingo_memes/backend
wincmd w
argglobal
if bufexists("~/code/django/bingo_memes/backend/pyproject.toml") | buffer ~/code/django/bingo_memes/backend/pyproject.toml | else | edit ~/code/django/bingo_memes/backend/pyproject.toml | endif
if &buftype ==# 'terminal'
  silent file ~/code/django/bingo_memes/backend/pyproject.toml
endif
balt ~/code/django/bingo_memes/backend/user/models.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 53 - ((52 * winheight(0) + 38) / 76)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 53
normal! 0
wincmd w
argglobal
if bufexists("~/code/django/bingo_memes/backend/backend/settings.py") | buffer ~/code/django/bingo_memes/backend/backend/settings.py | else | edit ~/code/django/bingo_memes/backend/backend/settings.py | endif
if &buftype ==# 'terminal'
  silent file ~/code/django/bingo_memes/backend/backend/settings.py
endif
balt ~/code/django/simplyhired_scraper/pyproject.toml
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 51 - ((50 * winheight(0) + 38) / 76)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 51
normal! 05|
lcd ~/code/django/bingo_memes/backend
wincmd w
exe 'vert 1resize ' . ((&columns * 94 + 142) / 284)
exe 'vert 2resize ' . ((&columns * 94 + 142) / 284)
exe 'vert 3resize ' . ((&columns * 94 + 142) / 284)
tabnext
edit ~/code/django/bingo_memes/backend/user/tests.py
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
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 70 - ((36 * winheight(0) + 38) / 76)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 70
normal! 0
wincmd w
argglobal
if bufexists("~/code/django/bingo_memes/backend/user/models.py") | buffer ~/code/django/bingo_memes/backend/user/models.py | else | edit ~/code/django/bingo_memes/backend/user/models.py | endif
if &buftype ==# 'terminal'
  silent file ~/code/django/bingo_memes/backend/user/models.py
endif
balt ~/code/django/bingo_memes/backend/user/tests.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
14
normal! zo
29
normal! zo
48
normal! zo
49
normal! zo
50
normal! zo
51
normal! zo
52
normal! zo
70
normal! zo
80
normal! zo
102
normal! zo
103
normal! zo
let s:l = 8 - ((7 * winheight(0) + 38) / 76)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 8
normal! 0
wincmd w
argglobal
if bufexists("~/code/django/bingo_memes/backend/user/api.py") | buffer ~/code/django/bingo_memes/backend/user/api.py | else | edit ~/code/django/bingo_memes/backend/user/api.py | endif
if &buftype ==# 'terminal'
  silent file ~/code/django/bingo_memes/backend/user/api.py
endif
balt ~/code/django/bingo_memes/backend/user/tests.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
33
normal! zo
41
normal! zo
50
normal! zo
let s:l = 11 - ((10 * winheight(0) + 38) / 76)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 11
normal! 037|
wincmd w
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
nohlsearch
let g:this_session = v:this_session
let g:this_obsession = v:this_session
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
