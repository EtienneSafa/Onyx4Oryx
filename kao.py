kaoLength=15


def kaoFace(str):
    kaoL=len(str)
    modulo=(kaoLength-kaoL)%2
    margin=int((kaoLength-kaoL)/2)
    print('|' + margin*'-' + modulo*'-' + str + margin*'-' + '|')
    

Nerdy = kaoFace('(⌐■_■)')

Happy = kaoFace("╰(*°▽°*)╯")

Jaded = kaoFace("'￣へ￣")

Angry = kaoFace("o(≧口≦)o")

Techy = kaoFace("ㄟ( ▔, ▔ )ㄏ")

Savvy = kaoFace("(￣y▽￣)╭")