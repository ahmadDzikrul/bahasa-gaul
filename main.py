meme_dict = {
    'gabut' : 'tidak ada kegiatan',
    'kepo' : 'pengen tau aja',
    'mantul' : 'mantap betul',
    'gercep': 'gerak cepet',
    'jamber' : 'jam berapa',
    'santuy' : 'santai',
    'ygy' : 'ya guys ya',
    'tbl' : 'takut banget lho',
    'gaje' : 'gak jelas'
}

for i in range(5):
    word = input("Ketik kata yang tidak kamu mengerti: ")
    if word in meme_dict.keys():
        # Apa yang harus kita lakukan jika kata itu ditemukan?
        print(meme_dict[word])
    else:
        # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
        print('kata gaul tersebut tidak ada di kamus')
