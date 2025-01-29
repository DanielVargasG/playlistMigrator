import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

class SpotifyAuth:    

    def __init__(self, scope):
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.redirect_uri = os.getenv("REDIRECT_URI")
        self.scope = scope
        self.sp = None

        # Validar si las variables de entorno están presentes
        if not self.client_id or not self.client_secret or not self.redirect_uri:
            raise ValueError("Faltan algunas variables de entorno necesarias: CLIENT_ID, CLIENT_SECRET, REDIRECT_URI.")

    def authenticate(self):
        """Autentica al usuario y guarda el cliente autenticado."""
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope=self.scope
        ))
        return self.sp