# code from the article https://realpython.com/factory-method-python/
# Isaac Rodriguez

import json
import yaml # pip install PyYAML
import xml.etree.ElementTree as et


class JsonSerializer:
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }
    
    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:
    def __init__(self):
        self._element = None
    
    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})
    
    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value
    
    def to_str(self):
        return et.tostring(self._element, encoding="unicode")


class YamlSerializer(serializers.JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)

class Song:
    """Concrete implementation of serializable -- product"""
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist
    
    def serialize(self, serializer):
        """Implementation of the interface Serializable
        without any knowledge of the format
        doesn't even know its goal is to convert to str
        """
        serializer.start_object('song', self.song_id)
        serializer.add_property('title', self.title)
        serializer.add_property('artist', self.artist)


class ObjectSerializer:
    """Implementation of the -- client"""
    def serialize(self, serializable, format):
        """Generic implementation of ObjectSerializer
        Arguments:
        ----------
        format: str
            Identify concrete implementation of `Serializer`
            Resolved by the `factory` object
        serializable: Serializable
            Abstract interface implemented on any object type
            That we want to serialize

        Returns: str serialized in the chosen format
        """
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()


class SerializerFactory:
    def __init__(self):
        """Stores registration of formats"""
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        """Possible because all Serializer* Classes provide
        .__init__() method to initialize the instances"""
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()

        # if format == "JSON":
        #     return JsonSerializer()
        # elif format == "XML":
        #     return XmlSerializer()
        # else:
        #     raise ValueRrror(format)

factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)
factory.register_format("YAML", YamlSerializer)

if __name__ == "__main__":
    song = Song('1', 'Ever Dream', 'Nightwish')
    serializer = ObjectSerializer()

    result_json = serializer.serialize(song, 'JSON')
    result_xml = serializer.serialize(song, 'XML')
    result_yaml = serializer.serialize(song, 'YAML')
    print(result_json, "\n", result_xml, "\n", result_yaml)
