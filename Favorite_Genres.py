from Helpers import profiler as prof
from Helpers import helper as hlp


class Solution:

    #def __init__(self):
    #    self.genres = {}

    def get_genres(self, userSongs, songGenres):
        lookup = {}

        output = {}
        for user in userSongs:
            if user not in output:
                output[user] = {}
            # problem
            for song in userSongs[user]:
                # cashed
                if song in lookup:
                    genre = lookup[song]
                    self.inc_genre(user, genre, output)
                else:
                    for genre in songGenres:
                        for g_song in songGenres[genre]:
                            lookup[g_song] = genre
                            if song == g_song:
                                self.inc_genre(user, genre, output)
                                break
            output[user] = self.fav_genres(output[user])
        return output

    def inc_genre(self, user, genre, userGenres):
        if genre not in userGenres[user]:
            userGenres[user][genre] = 0
        userGenres[user][genre] += 1

    def get_genres2(self, userSongs, songGenres):
        output = {}
        for user in userSongs:
            if user not in output:
                output[user] = {}
            for song in userSongs[user]:
                for genre in songGenres:
                    for g_song in songGenres[genre]:
                        if song == g_song:
                            if genre not in output[user]:
                                output[user][genre] = 0
                            output[user][genre] += 1
                            break
           # output[user] = self.fav_genres(output[user])
        return output

    def fav_genres(self, userGenres):
        fav_count = 0
        fav_genres = []
        for genre in userGenres:
            if userGenres[genre] > fav_count:
                fav_count = userGenres[genre]

        for genre in userGenres:
            if userGenres[genre] == fav_count:
                fav_genres.append(genre)
        return fav_genres


def run(parms):
    sl = Solution()

    res = sl.get_genres(parms[0], parms[1])
    print(res)


userSongs = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma": ["song5", "song6", "song7"]
}
songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

def build_genres(genres_count, songs_count):
    songGenres = {}
    for i in range(genres_count):
        genre_name = 'genre'+ str(i)
        songGenres[genre_name] = []
        for j in hlp.generate_array(10,songs_count):
            song_name = 'song' + str(j)
            songGenres[genre_name].append(song_name)
    return songGenres

def build_userSongs(users_count, user_songs_count, songGenres, songs_count):
    userSongs = {}
    for i in range(users_count):
        user_name = 'user' + str(i)
        userSongs[user_name] = []
        genre = hlp.generate_array(len(songGenres),1)[0]
        genre_name = 'genre' + str(genre)

        for j in hlp.generate_array(songs_count,user_songs_count):
            userSongs[user_name].append(songGenres[genre_name][j])
    return userSongs

songs_count = 600
genres_count = 100
songGenres2 = build_genres(genres_count,songs_count)
#print(songGenres2)
userSongs2 = build_userSongs(50, 1500, songGenres2, songs_count)
#print(userSongs2)
#prof.profile(run, userSongs, songGenres)
prof.profile(run, userSongs2, songGenres2)
