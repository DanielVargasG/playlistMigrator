from auth import SpotifyAuth

# Configuración inicial
SCOPE = "playlist-read-private"

def main():
    # Probar autenticación
    try:
        auth = SpotifyAuth(SCOPE)
        sp = auth.authenticate()
        print("Autenticación exitosa. Usuario autenticado correctamente.")

        # Obtener información básica del usuario autenticado
        user_info = sp.current_user()
        print(f"Nombre del usuario: {user_info['display_name']}")
        print(f"ID del usuario: {user_info['id']}")
    except Exception as e:
        print("Error durante la autenticación:", e)

if __name__ == "__main__":
    main()
