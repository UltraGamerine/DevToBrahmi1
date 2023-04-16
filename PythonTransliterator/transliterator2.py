#Brahmi <-> Devanagari Transliterator

import re

dv = '।॥०१२३४५६७८९अंआःइँईउऊएऐओऔक्खागिघीङुञूणेनैमोचौछृजॄझॢटॣठडढतथदधपफबभयरलळवशषसह'
br = '𑁇𑁈𑁦𑁧𑁨𑁩𑁪𑁫𑁬𑁭𑁮𑁯𑀅𑀁𑀆𑀂𑀇𑀀𑀈𑀉𑀊𑀏𑀐𑀑𑀒𑀓𑁆𑀔𑀸𑀕𑀺𑀖𑀻𑀗𑀼𑀜𑀽𑀡𑁂𑀦𑁃𑀫𑁄𑀘𑁅𑀙𑀾𑀚𑀿𑀛𑁀𑀝𑁁𑀞𑀟𑀠𑀢𑀣𑀤𑀥𑀧𑀨𑀩𑀪𑀬𑀭𑀮𑀴𑀯𑀰𑀱𑀲𑀳'

def Trans(mode:str,svar:int):
    trans = {}
    match mode:
        case 'dev_br': 
            trans = dict(zip(dv,br)) #dev to br
            trans['़'] = ""

        case 'br_dev' :
            trans = dict(zip(br,dv)) #br to dev

    if mode=='dev_br': # dev to br
        match svar:
            case 1: #vedic to vedic
                trans['\u0951'] ='\u0951'; trans['\u0952']='\u0952'
            case 2: #vedic to arrow
                trans['\u0951'] ='\u2191'; trans['\u0952']='\u2193'
            case 3: #vedic to None
                trans['\u0951'] =''; trans['\u0952']=''
            case _:
                pass

    if mode=='br_dev': # br to dev
        match svar:
            case 1: #vedic to vedic
                trans['\u0951'] ='\u0951'; trans['\u0952']='\u0952'
            case 2: #arrow to vedic
                trans['\u2191'] ='\u0951'; trans['\u2193']='\u0952'
            case 3: #arrow to None:
                trans['\u2193'] =''; trans['\u2191']=''
            case _:
                pass
            
    return trans

def br_dev(text, trans):
    #brahmi split pattern
    ak= "|".join(br)
    omPat=fr"(?<!{ak})𑀑𑀁(?!{ak})"
    pat = '(' + omPat + r"|\s|\n|\t" +')'
    print(pat)

    x = list(filter(None,re.split(pat,text)))

    #om handling
    x = ['ॐ' if i == '𑀑𑀁' else i for i in x]
    
    x = ''.join(["".join([trans[chr] if chr in trans else chr for chr in word])for word in x])

    print(x)
    return x

def dev_br(text, trans):
    # devanagari split pattern
    pat = '(' + "ॐ|\s|\n|\t" +')'
    print(pat)

    x = list(filter(None,re.split(pat,text)))

    #om handling
    x = ['𑀑𑀁' if i == 'ॐ' else i for i in x]
    
    x = ''.join(["".join([trans[chr] if chr in trans else chr for chr in word])for word in x])

    print(x)
    return x

def menu():
    try:
        modech = int(input('''
                            1. Devanagari To Brahmi
                            2. Brahmi To Devanagari
                            :'''))
        svarch = int(input('''
                            Svara - 
                            1. Vedic <-> Vedic
                            2. Arrow <-> Vedic
                            3. No Svara / Remove Svara
                            :'''))
    except: 
        zzz=input('\n\ntry again ...')
        return None

    match modech:
        case 1: # dev to br
            with open('dev.txt','r',encoding='utf-8') as devfile:
                with open('br.txt','w',encoding='utf-8') as brfile:
                    readtxt = devfile.read()
                    brfile.write(dev_br(readtxt,Trans('dev_br',svarch)))

        case 2: # br to dev
            with open('br.txt','r',encoding='utf-8') as brfile:
                with open('dev.txt','w',encoding='utf-8') as devfile:
                    readtxt = brfile.read()
                    devfile.write(br_dev(readtxt,Trans('br_dev',svarch)))

    zzz = input('\n           Transliteration Done ! ...')

menu()





















'''with open('br.txt','w', encoding='utf-8') as fileBr:
    fileBr.write(br_dev())
    
    if mode=='dev_br': # dev to br
        match svar:
            case 1: #vedic to vedic
                trans['\u0951'] ='\u0951'; trans['\u0952']='\u0952'
            case 2: #vedic to arrow
                trans['\u0951'] ='\u2193'; trans['\u0952']='\u2191'
            case 3: #vedic to None
                trans['\u0951'] =''; trans['\u0952']=''
            case _:
                pass

    if mode=='br_dev': # br to dev
        match svar:
            case 1: #vedic to vedic
                trans['\u0951'] ='\u0951'; trans['\u0952']='\u0952'
            case 2: #vedic to arrow
                trans['\u0951'] ='\u2193'; trans['\u0952']='\u2191'
            case 3: #arrow to vedic
                trans['\u2193'] ='\u0951'; trans['\u2191']='\u0952'
            case 4: #vedic to None
                trans['\u0951'] =''; trans['\u0952']=''
            case 5: #arrow to None:
                trans['\u2193'] =''; trans['\u2191']=''
            case _:
                pass
    
    
    '''
