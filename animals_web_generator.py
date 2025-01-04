import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def read_animals_html(file_path):
    with open(file_path, "r") as handle:
        return handle.read()

def print_animals_info(animals):
    output = ""
    for animal in animals:
        animal_type = animal["characteristics"].get("type")
        output += f"Name: {animal['name']}\n"
        output += f"Diet: {animal['characteristics']['diet']}\n"
        output += f"First location: {animal["locations"][0]}\n"
        if animal_type is not None:
            output += f"Type: {animal_type}\n"
        output += f"\n"
    return output

def write_new_content(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)

def main():
    animals_data = load_data("animals_data.json")
    html_content = read_animals_html("animals_template.html")

    new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__",
                                            print_animals_info(animals_data))
    write_new_content("animals.html", new_html_content)





if __name__ == "__main__":
    main()