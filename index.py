import os
import json

# Ruta al archivo original
INPUT_JSON = 'countries.json'
OUTPUT_DIR = 'output'

# Cargar todos los países
with open(INPUT_JSON, 'r', encoding='utf-8') as f:
    countries = json.load(f)

countries_only = []

for country in countries:
    country_name = country['name']
    country_dir = os.path.join(OUTPUT_DIR, country_name)
    os.makedirs(country_dir, exist_ok=True)

    # Guardar datos del país sin los estados
    country_data = {k: v for k, v in country.items() if k != 'states'}
    countries_only.append(country_data)

    states = country.get('states', [])

    # Lista para guardar estados sin ciudades
    states_without_cities = []

    for state in states:
        # Estado con ciudades
        state_with_cities = {
            'id': state['id'],
            'name': state['name'],
            'state_code': state['state_code'],
            'cities': state.get('cities', [])
        }

        # Guardar archivo del estado
        filename = f"{state['name'].replace('/', '-')}.json"
        filepath = os.path.join(country_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(state_with_cities, f, ensure_ascii=False, indent=2)

        # Estado sin ciudades para el archivo estados.json
        state_without_cities = {
            'id': state['id'],
            'name': state['name'],
            'state_code': state['state_code']
        }
        states_without_cities.append(state_without_cities)

    # Guardar el archivo estados.json
    with open(os.path.join(country_dir, 'estados.json'), 'w', encoding='utf-8') as f:
        json.dump(states_without_cities, f, ensure_ascii=False, indent=2)

# Guardar archivo de países
with open(os.path.join(OUTPUT_DIR, 'paises.json'), 'w', encoding='utf-8') as f:
    json.dump(countries_only, f, ensure_ascii=False, indent=2)
