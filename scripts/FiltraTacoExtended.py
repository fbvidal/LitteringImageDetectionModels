from pathlib import Path
import shutil
import json
import re

arquivo = Path("./annotations_artigo/annotations_train.json").open()
annotation_train = json.load(arquivo)
arquivo.close()
arquivo = Path("./annotations_artigo/annotations_test.json").open()
annotation_test = json.load(arquivo)
arquivo.close()



p = re.compile('^dumped/.+\.(jpeg|png|jpg)$')

Path("./dumped/train").mkdir(parents=True, exist_ok=True)
Path("./dumped/test").mkdir(parents=True, exist_ok=True)

#mkdir o "dumped"
for a in [image for image in annotation_test["images"] if p.match(image["file_name"])]:
    b = a["file_name"].split("/")[-1]
    if Path("./temp/"+b).is_file():
        shutil.move(f"./temp/{b}", f"./dumped/test/{b}")

print("Test finish")

for a in [image for image in annotation_train["images"] if p.match(image["file_name"])]:
    b = a["file_name"].split("/")[-1]
    if Path("./temp/"+b).is_file():
        shutil.move(f"./temp/{b}", f"./dumped/train/{b}")

print("Train finish")

