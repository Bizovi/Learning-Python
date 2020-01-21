# code from the article https://realpython.com/factory-method-python/
# Isaac Rodriguez
# a mock music API integration

class SpotifyService:
    def __init__(self, access_code):
        self._access_code = access_code
    
    def test_connection(self):
        print(f"Accessing spotify with {self._access_code}")


class SpotifyServiceBuilder:
    """Keeps the service instance around and only creates a new one
    if it's the first time it's requested"""
    def __init__(self):
        self._instance = None

    def __call__(self, spotify_client_key, spotify_client_secret, **_ignored):
        """Create and initialize concrete SpotifyService
        Specifies required params, ignores others **_ignored"""
        if not self._instance:
            access_code = self.authorize(
                spotify_client_key, spotify_client_secret
            )
            self._instance = SpotifyService(access_code)
        # creates and returns instance once access_code retrieved
        return self._instance
    
    def authorize(self, key, secret):
        return "SPOTIFY_ACCESS_CODE"


class PandoraService:
    def __init__(self, consumer_key, consumer_secret):
        self._key = consumer_key
        self._secret = consumer_secret

    def test_connection(self):
        print(f"Accessing Pandora with {self._key} and {self._secret}")


class PandoraServiceBuilder:
    """Same interface, different params and processes to create and 
    initialize the PandoraService. Keeps instance around, auth once"""
    def __init__(self):
        self._instance = None
    
    def __call__(self, pandora_client_key, pandora_client_secret, **_ignored):
        if not self._instance:
            consumer_key, consumer_secret = self.authorize(
                pandora_client_key, pandora_client_secret
            )
            self._instance = PandoraService(consumer_key, consumer_secret)
        return self._instance
    
    def authorize(self, key, secret):
        return "PANDORA_CONSUMER_KEY", "PANDORA_CONSUMER_SECRET"


class LocalService:
    def __init__(self, location):
        self._location = location
    
    def test_connection(self):
        print(f"Accessing local music at {self._location}")


def create_local_music_service(local_music_location, **_ignored):
    """Matches the interface of .__call__()"""
    return LocalService(local_music_location)


class ObjectFactory:
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        """Builder parameter can be any kind of object
        that implements callable interface .__call__()"""
        self._builders[key] = builder
    
    def create(self, key, **kwargs):
        """Additional arguments specified by kwargs
        Allows the builder object to specify params they need
        and ignore the rest in no particular order"""
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)


# specializing the object factory
class MusicServiceProvider(ObjectFactory):
    def get(self, service_id, **kwargs):
        return self.create(service_id, **kwargs)


services = MusicServiceProvider()
services.register_builder('SPOTIFY', SpotifyServiceBuilder())
services.register_builder('PANDORA', PandoraServiceBuilder())
services.register_builder('LOCAL', create_local_music_service) # fn is callables


if __name__ == "__main__":
    config = {
        'spotify_client_key': 'THE_SPOTIFY_CLIENT_KEY',
        'spotify_client_secret': 'THE_SPOTIFY_CLIENT_SECRET',
        'pandora_client_key': 'THE_PANDORA_CLIENT_KEY',
        'pandora_client_secret': 'THE_PANDORA_CLIENT_SECRET',
        'local_music_location': '/usr/data/music'
    }

    pandora = services.get('PANDORA', **config)
    pandora.test_connection()

    spotify = services.get('SPOTIFY', **config)
    spotify.test_connection()

    local = services.get("LOCAL", **config)
    local.test_connection()

    pandora2 = services.get('PANDORA', **config)
    print(f'id(pandora) == id(pandora2): {id(pandora) == id(pandora2)}')

    spotify2 = services.get('SPOTIFY', **config)
    print(f'id(spotify) == id(spotify2): {id(spotify) == id(spotify2)}')
