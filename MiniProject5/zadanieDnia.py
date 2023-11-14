import argparse
import json
import io
from functools import reduce


def delete_output(cell):
    if cell["cell_type"] == "code":
        cell["outputs"] = []
    return cell


def reducing_function(cells_list, cell2):
    if cells_list != []:
        if cells_list[-1]["cell_type"] == "markdown":
            for item in cells_list[-1]["source"]:
                if "# Ćwiczenie" in item and cell2["cell_type"] == "code":
                    cell2["source"] = []
    cells_list.append(cell2)
    return cells_list


parser = argparse.ArgumentParser()
parser.add_argument("input_file")
args = parser.parse_args()
input_path = args.input_file
filename=input_path.split(".")[0]
print(input_path)

with io.open(input_path, encoding='utf-8-sig') as json_data:
    data = json.loads(json_data.read())

print(data["cells"])
lista_komorek = data["cells"]
zmieniona_lista = list(map(delete_output, lista_komorek))
zredukowana_lista = reduce(reducing_function, zmieniona_lista, [])
data["cells"]=zredukowana_lista

with open(filename+'.czysty.ipynb', 'w') as outfile:
    json.dump(data, outfile)
