class PlaylistManager:
    def __init__(self, sp):
        """Inicializa con una instancia autenticada de spotipy."""
        self.sp = sp

    def get_playlist_info(self, playlist_id):
        """Obtiene información básica de una playlist."""
        playlist = self.sp.playlist(playlist_id)
        return {
            "name": playlist["name"],
            "description": playlist["description"],
            "tracks": [
                {
                    "title": track["track"]["name"],
                    "artist": track["track"]["artists"][0]["name"],
                }
                for track in playlist["tracks"]["items"]
            ],
        }

    def show_playlist_info(self, playlist_id):
        """Imprime la información de una playlist de forma organizada."""
        info = self.get_playlist_info(playlist_id)
        print(f"Nombre de la playlist: {info['name']}")
        print(f"Descripción: {info['description']}")
        print("Canciones:")
        for idx, track in enumerate(info["tracks"]):
            print(f"{idx + 1}. {track['title']} - {track['artist']}")

    def get_track_ids(self, playlist_id):
        """Devuelve solo los IDs de las canciones de una playlist."""
        playlist = self.sp.playlist(playlist_id)
        return [track["track"]["id"] for track in playlist["tracks"]["items"]]

    def get_playlist_owner(self, playlist_id):
        """Obtiene el nombre del usuario dueño de la playlist."""
        playlist = self.sp.playlist(playlist_id)
        return playlist["owner"]["display_name"]
    
    def list_playlists(self, show_private=True):
        """
        Lista las playlists del usuario autenticado.
        
        Parámetros:
        - show_private (bool): Si es True, muestra playlists privadas y públicas. 
          Si es False, solo muestra las públicas.

        Retorna:
        - Lista de diccionarios con nombre, ID y visibilidad de cada playlist.
        """
        playlists = []
        results = self.sp.current_user_playlists()  # Obtiene todas las playlists

        for playlist in results["items"]:
            playlist_info = {
                "name": playlist["name"],
                "id": playlist["id"],
                "is_public": playlist["public"],  # True = pública, False = privada
                "owner_display_name": playlist["owner"]["display_name"]
            }

            if show_private or playlist_info["is_public"]:
                playlists.append(playlist_info)

        return playlists
