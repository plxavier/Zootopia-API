import json

file_path = 'animals_data.json'


def load_data(file_path):
  """ Loads a JSON file """
  try:
      with open(file_path) as json_file:
          data = json.load(json_file)
          return data

  except FileNotFoundError:
      print('File not found')
      return None
  except Exception as e:
      print(f"The error is {e}")
      return None

animals_data = load_data('animals_data.json')
#print(animals_data) #prints the whole nested data; remove # to print


def print_data(data):
    """optional accessing and checking data in json"""
    try:
        for animal in animals_data:
            print(f"Name: {animal['name']}\n"
                  f"Diet: {animal['characteristics'].get('diet', 'N/A')}\n"
                  f"Location: {', '.join(animal['locations']) if animal['locations'] else "N/A"}\n"
                  f"Type: {animal['characteristics'].get('type', 'N/A')}"
                  f"\n"
                  )
    except Exception as e:
        print(f"The error is {e}")

    #print_data(animals_data) #remove # to print the data with selected key values


def serialize_animal(animal):
    """serializes animal in json"""
    output = ''  # empty string initiation
    output += '<li class="cards__item">\n'
    output += f' <div class="card__title">{animal['name']}</div>\n'
    output += '  <div class="card__text">\n'
    output += '    <ul class="card__attributes">\n'
    output += (f'    <li class="card__attribute"><strong>Diet:</strong> '
               f'{animal["characteristics"].get("diet", "N/A")}</li>\n')
    output += (f'    <li class="card__attribute"><strong>Location:</strong> '
               f'{', '.join(animal["locations"]) if animal["locations"] else "N/A"}</li>\n')
    output += (f'    <li class="card__attribute"><strong>Type:</strong> '
               f'{animal["characteristics"].get("type", "N/A")}</li>\n')
    output += (f'    <li class="card__attribute"><strong>Slogan:</strong> '
               f'{animal["characteristics"].get("slogan", "N/A")}</li>\n') #additional field
    output += (f'    <li class="card__attribute"><strong>Lifespan:</strong> '
               f'{animal["characteristics"].get("lifespan", "N/A")}</li>\n') #additional field
    output += '    </ul>\n'
    output += '  </div>\n'
    output += '</li>\n'

    return output


def generate_html(animal_data):
    """generates html page with serialized animal data"""
    try:
        with open('animals_template.html', 'r') as template:
            animals_template = template.read()

        output = ""

        for animal in animal_data:
            output += serialize_animal(animal)

        html_content = animals_template.replace('__REPLACE_ANIMALS_INFO__', output)

        with open('animals.html', 'w') as output_file:
            output_file.write(html_content)

        print("animals.html created successfully")
        return html_content #return html content too for optional downstream processing

    except FileNotFoundError:
        print("animals_template.html not found")
        return None
    except Exception as e:
        print(f"The error is {e}")
        return None


def main():
    """main function to call serialize_animal function and generate html page"""
    try:
        if animals_data:
            html_content = generate_html(animals_data)

            if not html_content:
                print(f"Failed to generate html page")
            else:
                print(f"Successfully generated animal repository html page "
                      f"with {(html_content.count('\n'))} lines "
                      f"for {len(animals_data)} animals")
        else:
            print("No animals data found")
    except Exception as e:
        print(f"The error is {e}")


if __name__ == "__main__":
    main()