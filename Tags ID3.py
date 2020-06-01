import mutagen
import mutagen.id3

# testFile = '/home/aymeric/Musique/10. Caustic Are The Ties That Bind.mp3'
# testFile2 = '/home/aymeric/Musique/04 Lonkkaluut.mp3'
# testFile3 = '/home/aymeric/Musique/04 Lonkkaluut modif.mp3'

# img1 = '/home/aymeric/Images/Kirby assassin 800x800.jpg'
# img2 = '/home/aymeric/Images/Kirby assassin 800x800.png'

if __name__ == "__main__":
    test_1 = "08 The Berserker at Stamford Bridge.mp3"
    # test_1 = "09. Remembrance Day.mp3"

    # audio = mutagen.File(test_1)
    # tags = audio.tags
    tags = mutagen.id3.ID3(test_1)

    # print(tags)
    # print("---")
    #
    print(tags.pprint())
    #
    # for a in tags:
    #     print(a, tags[a])

# add ID3 tag if it doesn't exist
# try:
#     audio.add_tags()
# except mutagen.id3.error:
#     pass
#
# audio.tags.add(
#     mutagen.id3.APIC(
#         encoding=3, # 3 is for utf-8
#         mime='image/png', # image/jpeg or image/png
#         type=3, # 3 is for the cover image
#         desc=u'Cover',
#         data=open(img2).read()
#     )
# )
# audio.save()

# f = mutagen.File(testFile3)
# artwork = f.tags['APIC:'].data
# img = open('image.jpg', 'wb')
# img.write(artwork)

# audio.tags.update_to_v23()
# save(v2_version=3)

# attributs d'un MP3 mutagen.mp3 : info.length, info.bitrate




# import taglib

# t1 = taglib.File('/home/aymeric/Musique/10. Caustic Are The Ties That Bind.mp3')

# print(t1.tags)

# def save_tags(t):
#     ret = t.save()
#     if ret != {}:
#         print('! Non enregistrés :',ret)
#     return None



# attributs d'un File taglib : tags, length, sampleRate, channels, bitrate, readOnly


# from myModules.commandes import Commande
# from myModules.classiques import lister_dossiers
# import os
# import os.path as op
# from subprocess import call, check_output, STDOUT
# import taglib


# def to_mp3(ini,out,bitrate='320k',avertir=True,base=''):
#     end = ['-threads','auto','-y','-loglevel','quiet',out]
#     if avertir:
#         c = Commande(['avconv','-i',ini,'-c:a','libmp3lame','-ab',bitrate]+end)
#         c.pcall()
#         print('Fichier {} créé !'.format(op.relpath(out,base)))
#     else:
#         c = Commande(['avconv','-i',ini,'-c:a','libmp3lame','-ab',bitrate]+end)
#         c.call()


# def parametres_audio(f):
#     duration,bitrate = '',''
#     c = Commande(['avprobe',f])
#     a = c.check_output().split('\n')
#     b0 = [l for l in a if 'Duration:' in l]
#     if b0 == []:
#         raise ValueError("Bitrate non trouvé !")
#     ligne = b0[0]
#     while ligne != '' and ligne[0] == ' ':
#         ligne = ligne[1:]
#     b1 = ligne.split(', ')
#     # [Duration: xxx, start: xxx, bitrate: xxx] ou [Duration: xxx, bitrate: xxx]
#     duration = [x for x in b1 if 'Duration: ' in x][0][10:]
#     bitrate = [x for x in b1 if 'bitrate: ' in x][0][9:-5]+'k'
#     return duration,bitrate


# def adapt_bitrate(b):
#     """adapte le bitrate '...k' vers une puissance de 2"""
#     bn = int(b[:-1]) # sans le 'k'
#     bs = [64,128,192,256,320]
#     c = 0
#     continuer = True
#     while c < 5 and continuer:
#         if bs[c]+3 >= bn: # petite marge
#             bn = bs[c]
#             continuer = False
#         c += 1
#     bn = min(bn,320)
#     return str(bn)+'k'

# def move_to_not_mp3(f,d1,d2=''):
#     """déplace le morceau vers un dossier dédié aux non mp3s, de d1 vers d2"""
#     if d2 != '': # évite désastre...
#         f2 = op.join(d2,op.relpath(f,d1))
#         os.renames(f,f2)


# def go_folder(folder,base='',f_nonmp3=''):
#     action = False
#     conv_ext = ['.wma','.m4a','.wav','.flac'] # à convertir
#     norm_ext = ['.wma','.m4a','.wav','.flac','.mp3','.jpg','.jpeg','.png','.txt']
#     l0 = sorted([f for f in os.listdir(folder) if f[0] != '.'])
#     l1 = [op.join(folder,f) for f in l0]
#     l2 = [f for f in l1 if op.isfile(f)]
#     for f in l2:
#         ext = op.splitext(f)[1]
#         if ext.lower() not in norm_ext:
#             print('! Extension étrange : {}'.format(op.relpath(f,base)))
#         if ext != '.mp3' and ext.lower() == '.mp3':
#             os.rename(f,op.splitext(f)[0]+'.mp3')
#             print('- Fichier {} renommé !'.format(op.relpath(f,base)))
#     l3 = [f for f in l2 if op.splitext(f)[1] in conv_ext]
#     for f in l3:
#         print('# Conversion : {}'.format(op.relpath(f,base)))
#         action = True
#         bitrate = parametres_audio(f)[1]
#         bitrate2 = adapt_bitrate(bitrate)
#         print('- bitrate initial : {} ; bitrate adapté : {}'.format(bitrate,bitrate2))
#         f2 = op.splitext(f)[0]+'.mp3'
#         to_mp3(f,f2,bitrate2,False,base)
#         print('- Fichier {} créé !'.format(op.relpath(f2,base)))
#         # tags manquants
#         t1 = taglib.File(f)
#         t2 = taglib.File(f2)
#         for key in [key for key in t1.tags if not key in t2.tags]:
#             t2.tags[key] = t1.tags[key]
#         ret = t2.save()
#         if ret != {}:
#             print('! Non enregistrés :',ret)
#         # suppression de l'ancien
#         move_to_not_mp3(f,base,f_nonmp3) # os.remove(f)
#         print('- Fichier {} déplacé !'.format(op.relpath(f,base)))
#     if action:
#         print('> Dossier {} fini !'.format(op.relpath(folder,base)))

# def go(dossier,f_nonmp3=''):
#     print('- Création de la liste des dossiers...')
#     dossiers = [op.join(dossier,d) for d in lister_dossiers(dossier)]
#     print('- Liste des dossiers générée !')
#     print('### Traitement du dossier {}'.format(dossier))
#     for d in dossiers: # ou dossiers[:limite]
#         go_folder(d,dossier,f_nonmp3)
#     print('### Tout fini ! ###')


# print('Go !')

# go('/media/aymeric/HDD ext. Aymeric/Musique autres','/media/aymeric/HDD ext. Aymeric/Non mp3s/Musique autres')

# go('/media/aymeric/HDD ext. Aymeric/Metal Symphonique','/media/aymeric/HDD ext. Aymeric/Non mp3s/Metal Symphonique')

# go('/media/aymeric/HDD ext. Aymeric/Metal (divers)','/media/aymeric/HDD ext. Aymeric/Non mp3s/Metal (divers)')



# test = "/home/aymeric/Dusk Dismantled.mp3"

# f = taglib.File(test)
# f.tags
# f.save()

# print('bitrate :',parametres_audio(test)[1])

# avconv -i input.wav -metadata title="track title" -metadata author="track artist" -metadata album="album name" -metadata track="track number" output.flac


# d = "/media/aymeric/HDD ext. Aymeric/Metal (divers)"
# f1 = d+"/Children Of Bodom/2005 - Are You Dead Yet/01. Living Dead Beat.wma"
# f2 = d+"/Children Of Bodom/2005 - Are You Dead Yet/01. Living Dead Beat.mp3"
# t1 = taglib.File(f1)
# t2 = taglib.File(f2)
# print('\nt1 :\n',t1.tags,'\nt2 :\n',t2.tags)
