kaoLength=15


def kaoFace(str):
    kaoL=len(str)
    print(kaoL)
    modulo=(kaoLength-kaoL)%2
    print(modulo)
    margin=int((kaoLength-kaoL)/2)
    print(margin)
    print('|' + margin*'-' + modulo*'-' + str + margin*'-' + '|')
    

Nerdy = kaoFace('(⌐■_■)')

Happy = kaoFace("╰(*°▽°*)╯")

Jaded = kaoFace("'￣へ￣")

Angry = kaoFace("o(≧口≦)o")

Techy = kaoFace("ㄟ( ▔, ▔ )ㄏ")

Savvy = kaoFace("(￣y▽￣)╭")

print(Nerdy)
print(Happy)
print(Jaded)
print(Angry)
print(Techy)
print(Savvy)