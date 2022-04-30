'''
. - any symbol except \n
\d - any number in range 0 to 9
\D - any symbol 
\s - any space symbol(tab, backspace,\n,  ' ')
\S - any symbol except space symbols
\w - any alpha, digit or _ symbol(a-z, A-Z, 0-9, _)
\W - any symbol, except alpha, digit, or _ (comma, period, !, ?, \,/,{,})

'''

'''
merging symbols:
[a-zA-zА-я] - any symbol in []
[^a-z] - any symbol except a-z
[0-9A-Z] - al from 0 to 9 and from A to Z
[-0-9A-Z] - if you need -, then put it at the beginning or end
[\]\\] - if you need to find \ or ] or [  or ] then put \ before those symbols
(a|b) - one of the symbols inside ()
'''
'

'''
\b -   start or end of the string(\bstring- start, string\b- end)
\B - not the edges of the string
