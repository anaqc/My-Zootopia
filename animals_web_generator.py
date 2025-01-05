import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def read_animals_html(file_path):
    with open(file_path, "r") as handle:
        return handle.read()

def print_animals_info(animals):
    # define an empty string
    output = ""
    for animal in animals:
        animal_type = animal["characteristics"].get("type")
        # append information to each string
        output += "<li class='cards__item'>"
        output += f"Name: {animal['name']}<br/>\n"
        output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        output += f"First location: {animal["locations"][0]}<br/>\n"
        if animal_type is not None:
            output += f"Type: {animal_type}<br/>\n"
        output += f"</li>"
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