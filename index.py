import os
import json

# Ruta al archivo original con todos los países
INPUT_JSON = './countries.json'
OUTPUT_DIR = './output'

# Cargar el JSON global
with open(INPUT_JSON, 'r', encoding='utf-8') as f:
    countries = json.load(f)

# Lista para almacenar solo los países sin el campo "states"
countries_only = []

for country in countries:
    country_name = country['name']
    country_dir = os.path.join(OUTPUT_DIR, country_name)
    os.makedirs(country_dir, exist_ok=True)

    # Extraer todos los datos del país excepto "states"
    country_data = {k: v for k, v in country.items() if k != 'states'}
    countries_only.append(country_data)

    # Procesar los estados
    for state in country.get('states', []):
        state_data = {
            'id': state['id'],
            'name': state['name'],
            'state_code': state['state_code'],
            'cities': state.get('cities', [])
        }

        # Guardar el archivo del estado con su info y ciudades
        filename = f"{state['name'].replace('/', '-')}.json"  # evitar errores por '/'
        filepath = os.path.join(country_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(state_data, f, ensure_ascii=False, indent=2)

# Guardar los países sin estados
with open(os.path.join(OUTPUT_DIR, 'paises.json'), 'w', encoding='utf-8') as f:
    json.dump(countries_only, f, ensure_ascii=False, indent=2)
