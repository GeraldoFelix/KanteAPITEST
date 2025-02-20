import lyricsgenius
import json
import re

# Substitua 'YOUR_ACCESS_TOKEN' pelo seu token da API do Genius
genius = lyricsgenius.Genius()

def limpar_letra(lyrics):
    """Remove propagandas, traduções e textos desnecessários da letra."""
    lyrics = re.sub(r"Translations.*?\n", "", lyrics)  # Remove seções de tradução
    lyrics = re.sub(r"See .*? LiveGet tickets as low as .*?\n", "", lyrics)  # Remove anúncios de shows
    lyrics = re.sub(r"You might also like.*", "", lyrics, flags=re.DOTALL)  # Remove sugestões de músicas
    lyrics = re.sub(r"\d+Embed", "", lyrics)  # Remove qualquer número seguido de "Embed"
    lyrics = re.sub(r"\n{2,}", "\n", lyrics)  # Remove linhas vazias extras
    return lyrics.strip()

def get_lyrics(song_title, artist_name):
    try:
        song = genius.search_song(song_title, artist_name)
        if song:
            return limpar_letra(song.lyrics)  # Aplica a limpeza antes de retornar
        else:
            return "Letra não encontrada."
    except Exception as e:
        return f"Erro ao buscar a letra: {e}"

def save_lyrics_to_json(song_title, artist_name, filename="lyrics.json"):
    lyrics = get_lyrics(song_title, artist_name)
    data = {
        "title": song_title,
        "artist": artist_name,
        "lyrics": lyrics
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Letra salva em {filename}")

# Exemplo de uso
song_title = "LUTHER"
artist_name = "Kendrick Lamar"
save_lyrics_to_json(song_title, artist_name)
