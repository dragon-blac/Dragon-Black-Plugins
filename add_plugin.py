import json

# Archivo donde se guardarán los datos
FILE_JSON = "plugins.json"

# Intentar cargar datos existentes o crear lista vacía
try:
    with open(FILE_JSON, 'r', encoding='utf-8') as f:
        plugins_list = json.load(f)
    print(f"\033[31m✓ {len(plugins_list)} tools registered in the file.\033[31m")
except FileNotFoundError:
    plugins_list = []
    print("✓ new file")

# Pedir datos al usuario
print("\n" + "="*40)
print("data record")
print("="*40)

while True:
    print(f"\n \033[34mtools #{len(plugins_list) + 1}")
    print("-" * 20)
    name = input("Plugin name (no spaces, use hyphens or underscores: ").strip()
    if not name:
        print("❗the Plugin name should not be empty")
        break

    version = input("Plugin version: ").strip()
    if not version:
        print("❗the Plugin version should not be empty")
        break

    author = input("❗Plugin author (name): ").strip()
    if not author:
        print("❗the Plugin author should not be empty")
        break

    description = input("Plugin description ").strip()
    if not description:
        print("❗the Plugin description should not be empty")
        break

    source = input("Plugin source ejm(https://github.com/Brais-Moure/Dragon-Black): ").strip()
    if not source:
        print("❗the Plugin source should not be empty")
        break

    git_url = input("Plugin repo ejm(https://github.com/Brais-Moure/Dragon-Black): ").strip()
    if not git_url:
        print("❗the Plugin repo should not be empty")
        break

    command = input("Main command for the plugin [name]: ").strip()
    if not command:
        print("❗the Plugin command should not be empty") 
        break
    main = "plugin.py"
    default_function = "main"
        
    plugins_dict = {
        
        "name": name,
        "version": version,
        "author": author,
        "description": description,
        "source": source,
        "git_url": git_url,
        "main": main,
        "command": command,
        "default_function": default_function
      }
    
    
    plugins_list.append(plugins_dict)
    print(f"✅ {name.title()} tool add")
    break

# Guardar todos los datos
with open(FILE_JSON, 'w', encoding='utf-8') as f:
    json.dump(plugins_list, f, indent=4, ensure_ascii=False)
    print(f"\n!Your data was added correctly")
