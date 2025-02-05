import json
import yaml
import xml.etree.ElementTree as ET
import csv

def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def read_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def read_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return {child.tag: child.text for child in root}

def read_csv(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

if __name__ == "__main__":
    print("TXT Data:", read_txt("../data_files/data.txt"))
    print("JSON Data:", read_json("../data_files/data.json"))
    print("YAML Data:", read_yaml("../data_files/data.yaml"))
    print("XML Data:", read_xml("../data_files/data.xml"))
    print("CSV Data:", read_csv("../data_files/data.csv"))
