# code from the article https://realpython.com/factory-method-python/
# Isaac Rodriguez - basic implementation of factory method

from typing import (Callable)
import json 
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id: str, title: str, artist: str) -> None:
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song: Song, format: str) -> str:
        serializer = self._get_serializer(format)
        return serializer(song)

    def _get_serializer(self, format: str) -> Callable[[Song], str]:
        """Should be an external function. Doesn't depend on self"""
        if format == "JSON":
            return self._serialize_to_json
        elif format == "XML":
            return self._serialize_to_xml
        else:
            raise ValueError(format)
    
    def _serialize_to_json(self, song: Song) -> str:
        """Should be an external function. Doesn't depend on self"""
        payload = {
            "id": song.song_id,
            "title": song.title,
            "artist": song.artist
        }
        return json.dumps(payload)

    def _serialize_to_xml(self, song: Song) -> str:
        """Should be an external function. Doesn't depend on self"""
        song_element = et.Element('song', attrib={'id': song.song_id})

        title = et.SubElement(song_element, 'title')
        title.text = song.title

        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist

        return et.tostring(song_element, encoding='unicode')



if __name__ == "__main__":
    song = Song('1', 'Ever Green', 'Nightwish')
    serializer = SongSerializer()

    result_json: str = serializer.serialize(song, "JSON")
    result_xml: str = serializer.serialize(song, "XML")
    print(result_json, "\n", result_xml)