class SongRegisterController:
    def insert(self, new_song_informations: dict) -> dict:
        try:
            self.__verify_songs_infos(new_song_informations)
            self.__verify_if_song_already_exists(new_song_informations)
            self.__insert_song(new_song_informations)
            response = self.__format_response(new_song_informations)

            return response
        except Exception as exception:
            return self.__format_error_response(exception)

    def __verify_songs_infos(self, new_song_informations: dict) -> None:
        if len(new_song_informations['title']) > 100:
            raise Exception('Song title with more than 100 characters')

        year = int(new_song_informations['year'])
        if year > 2026:
            raise Exception('Invalid song year')

    def __verify_if_song_already_exists(self, new_song_informations: dict) -> None:
        pass

    def __insert_song(self, new_song_informations: dict) -> None:
        pass

    def __format_response(self, new_song_informations: dict) -> dict:
        return {
            "success": True,
            "count": 1,
            "attributes": {
                "title": new_song_informations['title']
            }
        }

    def __format_error_response(self, err: Exception) -> dict:
        return {
                "success": False,
                "error": str(err)
            }
