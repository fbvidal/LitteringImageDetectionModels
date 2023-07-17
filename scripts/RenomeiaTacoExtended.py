from pathlib import Path
import shutil
import json

arquivo = Path("Unoficial_taco.json").open()
annotation = json.load(arquivo)
arquivo.close()

pasta = Path("./unofficial")

Path("./temp").mkdir(parents=True, exist_ok=True)

#mkdir o "dumped"
for file in list(pasta.glob('*.jpg')):
    novo = next(image for image in annotation["images"] if image["file_name"] == "unofficial/" + file.name)["flickr_url"]
    novo = novo.split("/")[-1]
    antigo = file.name
    print(antigo + " -> " + novo)
    shutil.move(f"./unofficial/{antigo}", f"./temp/{novo}")
print("finish")
