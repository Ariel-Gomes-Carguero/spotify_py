# spotify_py
Script que cria playlists automaticas de acordo com gosto do usuário
Para usar o script é necessário gerar um token




Criação de Token para o campo "token" no cabeçalho


https://open.spotify.com/artist/2aKyKSggb31Kw9s9i3iXoo?si=j0g5jLU5Stu6nhplLqOZ5g



Pegar ID do usuário e de Artista


Seleciona seu usuário estando no app do spotify clique em "..." em seguida "Copiar url do spotify" depois de ":" é o id do seu user no meu caso é arielgs
No caso de Artista é o mesma coisa, busque o artista que deseja, entre no perfil, clique em "..." seguida "Copiar url do spotify" 
Virá algo semelhante spotify:artist:4vGrte8FDu062Ntj0RsPiZ, precisamos apenas do 4vGrte8FDu062Ntj0RsPiZ dentro da tag seed_artists = ''


Atributos personalizaveis


https://developer.spotify.com/documentation/web-api/reference/browse/get-recommendations/



Se seu código retornar 201 sua playlista está criada
