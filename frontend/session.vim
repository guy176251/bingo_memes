let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/code/django/bingo_memes/frontend
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +92 src/components/tile/index.tsx
badd +19 src/layouts/carddetail.tsx
badd +25 src/components/tile/navbar.tsx
badd +113 src/context/tiles.tsx
badd +63 src/context/auth.tsx
badd +42 src/components/card/info.tsx
badd +56 src/layouts/index.tsx
badd +114 src/components/card/tiles.tsx
badd +20 src/index.tsx
badd +8 src/layouts/test.tsx
badd +12 src/components/card/list.tsx
badd +28 src/components/card/const.tsx
argglobal
%argdel
tabnew +setlocal\ bufhidden=wipe
tabrewind
edit src/components/tile/index.tsx
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
exe 'vert 1resize ' . ((&columns * 93 + 140) / 280)
exe 'vert 2resize ' . ((&columns * 93 + 140) / 280)
exe 'vert 3resize ' . ((&columns * 92 + 140) / 280)
argglobal
balt src/layouts/carddetail.tsx
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=8
setlocal fml=1
setlocal fdn=20
setlocal fen
19
normal! zo
33
normal! zo
35
normal! zo
36
normal! zo
37
normal! zo
38
normal! zo
39
normal! zo
49
normal! zo
50
normal! zo
51
normal! zo
64
normal! zo
66
normal! zo
68
normal! zo
69
normal! zo
70
normal! zo
71
normal! zo
77
normal! zo
78
normal! zo
79
normal! zo
let s:l = 22 - ((20 * winheight(0) + 38) / 77)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 22
normal! 0
wincmd w
argglobal
if bufexists("src/layouts/carddetail.tsx") | buffer src/layouts/carddetail.tsx | else | edit src/layouts/carddetail.tsx | endif
if &buftype ==# 'terminal'
  silent file src/layouts/carddetail.tsx
endif
balt src/layouts/index.tsx
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
17
normal! zo
22
normal! zo
24
normal! zo
43
normal! zo
let s:l = 19 - ((18 * winheight(0) + 38) / 77)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 19
normal! 035|
wincmd w
argglobal
if bufexists("src/components/tile/navbar.tsx") | buffer src/components/tile/navbar.tsx | else | edit src/components/tile/navbar.tsx | endif
if &buftype ==# 'terminal'
  silent file src/components/tile/navbar.tsx
endif
balt src/components/tile/index.tsx
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=8
setlocal fml=1
setlocal fdn=20
setlocal fen
19
normal! zo
29
normal! zo
30
normal! zo
let s:l = 25 - ((13 * winheight(0) + 38) / 77)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 25
normal! 020|
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 93 + 140) / 280)
exe 'vert 2resize ' . ((&columns * 93 + 140) / 280)
exe 'vert 3resize ' . ((&columns * 92 + 140) / 280)
tabnext
edit src/context/tiles.tsx
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
exe 'vert 1resize ' . ((&columns * 93 + 140) / 280)
exe 'vert 2resize ' . ((&columns * 93 + 140) / 280)
exe 'vert 3resize ' . ((&columns * 92 + 140) / 280)
argglobal
balt src/layouts/carddetail.tsx
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
7
normal! zc
14
normal! zc
27
normal! zc
41
normal! zo
41
normal! zc
117
normal! zc
122
normal! zc
let s:l = 41 - ((40 * winheight(0) + 38) / 77)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 41
normal! 0
wincmd w
argglobal
if bufexists("src/layouts/index.tsx") | buffer src/layouts/index.tsx | else | edit src/layouts/index.tsx | endif
if &buftype ==# 'terminal'
  silent file src/layouts/index.tsx
endif
balt src/components/card/const.tsx
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
18
normal! zo
21
normal! zo
43
normal! zo
51
normal! zo
52
normal! zo
let s:l = 54 - ((53 * winheight(0) + 38) / 77)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 54
normal! 033|
wincmd w
argglobal
if bufexists("src/components/card/tiles.tsx") | buffer src/components/card/tiles.tsx | else | edit src/components/card/tiles.tsx | endif
if &buftype ==# 'terminal'
  silent file src/components/card/tiles.tsx
endif
balt src/components/card/info.tsx
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=10
setlocal fml=1
setlocal fdn=20
setlocal fen
88
normal! zo
let s:l = 125 - ((59 * winheight(0) + 38) / 77)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 125
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 93 + 140) / 280)
exe 'vert 2resize ' . ((&columns * 93 + 140) / 280)
exe 'vert 3resize ' . ((&columns * 92 + 140) / 280)
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
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
