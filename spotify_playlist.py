import requests
import json
token = "INSIRA O TOKEN GERADO"
endpoint = "https://api.spotify.com/v1/recommendations?"
user_id = "ID DO SEU PERFIL"
endpoint_playlist = f"https://api.spotify.com/v1/users/{user_id}/playlists"
lista = []

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}',
}

limit=10 #quantidade de musicas
market="" # Sigla do país por exemplo BR, US
seed_genres="" # Genero musical consulte a doc do spotify
energy=10.0 # Intensidade da música ex: Alta, barulhenta
valence=1.0  # Feeling transmitido pela musica ex: Alegria, tristeza, raiva)
seed_artists = '' #ID do artista que vc quer musicas semelantes
query = f'{endpoint}limit={limit}&market={market}&seed_genres={seed_genres}&energy={energy}&valence={valence}'
query += f'&seed_artists={seed_artists}'


response = requests.get(query, headers=headers)
resposta = response.json()
for i in resposta['tracks']:
    lista.append(i['uri'])


request_body = json.dumps({
    "name": "TITULO DA SUA PLAYLIST ",
    "description": "DESCRICAO DA SUA PLAYLIST",
    "public": False
})

testando = requests.post(url = endpoint_playlist, data = request_body, headers=headers)

playlist_id = testando.json()['id']

endpoint_list = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_musicas = json.dumps({
    "uris" : lista
        })


respondendo = requests.post(url = endpoint_list, data = request_musicas, headers=headers)

print(respondendo.status_code)
