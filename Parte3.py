# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:56:52 2024

@author: NANCY
"""

#EXTRACCIÓN DE TEXTO EN ARCHIVOS INDIVIDUALES DE ARCHIVOS HTML

import os
from lxml import etree
import lxml.html

script_dir = os.path.dirname(os.path.abspath(__file__))

# Directorio de destino para los archivos
data_folder = os.path.join(script_dir, "raw")

filenames = [os.path.join(data_folder, filename) for filename in os.listdir(data_folder)]

text_output_folder = os.path.join(script_dir, "websitesTextOnly")
# Crear el directorio si no existe
os.makedirs(text_output_folder, exist_ok=True)

skip_node_types = ["script", "head", "style", etree.Comment]

def get_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as inf:
        html_tree = lxml.html.parse(inf)
        return get_text_from_node(html_tree.getroot())

def get_text_from_node(node):
    if len(node) == 0:
        # No children, just return text from this item
        if node.text and len(node.text) > 100:
            return node.text
        else:
            return ""
    results = (get_text_from_node(child) for child in node if child.tag not in skip_node_types)
    return "\n".join(r for r in results if r is not None and len(r) > 1)  # Check if r is not None

for filename in os.listdir(data_folder):
    text = get_text_from_file(os.path.join(data_folder, filename))
    if text is not None:  # Check if text is not None before writing
        with open(os.path.join(text_output_folder, filename), 'w', encoding='utf-8') as outf:
            outf.write(text)
    else:
        print(f"No text found for file: {filename}")
