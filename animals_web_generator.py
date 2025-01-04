import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    animals_data = load_data("animals_data.json")
    for animal in animals_data:
        animal_type = animal["characteristics"].get("type")
        print(f"Name: {animal["name"]}")
        print(f"Diet: {animal["characteristics"]["diet"]}")
        print(f"First location: {animal["locations"][0]}")
        if animal_type is not None:
            print(f"Type: {animal_type}")
        print()


if __name__ == "__main__":
    main()