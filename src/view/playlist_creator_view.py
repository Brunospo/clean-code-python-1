import os

class PlaylistCreatorView:
    def playlist_creator_success(self, controller_response: dict) -> None:
        self.clear()
        print("Playlist Criada com Sucesso! \n\n")

        for music in controller_response["playlist"]:
            message = '''
                Titulo da musica: {}
                Artista: {}
                Ano de publicação: {}
            '''.format (
                music.title,
                music.artist,
                music.year
            )

            print (message)

    def playlist_creator_fail(self,controller_response: dict):
        message = '''
          Erro na criação da playlist:

          * Erro: {}
        '''.format(controller_response['error'])

        print(message)

    def clear(self):
        os.system("cls| |clear")
