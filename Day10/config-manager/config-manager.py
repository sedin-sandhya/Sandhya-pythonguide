import json
from pathlib import Path


DEFAULTS = {
    "theme": "light",
    "language": "en",
    "font_size": 14,
    "auto_save": True
}


class JsonFileStorage:

    def __init__(self, path):
        self.path = Path(path)


    def exists(self):
        return self.path.exists()


    def read(self):

        with open(self.path, "r") as file:
            return json.load(file)


    def write(self, data):

        with open(self.path, "w") as file:
            json.dump(data, file, indent=2)



class ConfigManager:

    def __init__(self, storage):

        self.storage = storage

        self.config = self.load_config()



    def load_config(self):

        if not self.storage.exists():

            self.storage.write(DEFAULTS)

            return DEFAULTS.copy()


        return self.storage.read()



    def get(self, key, default=None):

        return self.config.get(key, default)



    def set(self, key, value):

        self.config[key] = value

        self.storage.write(self.config)



    def delete(self, key):

        if key in self.config:

            del self.config[key]

            self.storage.write(self.config)

            return True


        return False



    def reset(self):

        self.config = DEFAULTS.copy()
        self.storage.write(self.config)



def main():

    storage = JsonFileStorage("config.json")

    config = ConfigManager(storage)


    print("Current theme:", config.get("theme"))
    config.set("theme", "dark")

    print("Updated theme:",config.get("theme"))
    config.set("font_size", 20)

    print("Font size:", config.get("font_size"))

    deleted = config.delete("language")
    print("Language deleted:", deleted)

    print("Language:", config.get("language", "Not Found"))
    config.reset()

    print("\nAfter reset:")

    print("Theme:", config.get("theme"))
    print("Language:", config.get("language"))
    print("Font size:", config.get("font_size"))



if __name__ == "__main__":
    main()