# import json
# path='{"module": "keras", "class_name": "DTypePolicy", "config": {"name": "float32"}, "registered_name": null}'
# correct = '"float32"'
# file_path = r"Project\218to215\model_config.json"

# with open(file_path,'r') as f:
#     content = json.load(f)

# content = str(content)
# content = content.replace(path,correct)
# print(content)
# with open(file_path,'w') as f:
#     content = f.write(content)

import json

# Ruta al archivo JSON del modelo
json_path = r"Project\218to215\model_config.json"

# Cargar el JSON
with open(json_path, 'r') as f:
    config = json.load(f)

def fix_dtype(obj):
    if isinstance(obj, dict):
        for key, value in list(obj.items()):
            if key == 'dtype' and isinstance(value, dict):
                if value.get('class_name') == 'DTypePolicy':
                    obj[key] = value['config']['name']
            else:
                fix_dtype(value)
    elif isinstance(obj, list):
        for item in obj:
            fix_dtype(item)

# Ejecutar la limpieza
fix_dtype(config)

# Guardar el JSON limpio
output_path = 'model_config_fixed.json'
with open(output_path, 'w') as f:
    json.dump(config, f, indent=4)

print(f"JSON corregido guardado en {output_path}")
