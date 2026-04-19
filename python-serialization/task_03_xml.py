#!/usr/bin/python3
"""
Module for serializing and deserializing dictionaries using XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the output XML file.
    """
    # Create the root element <data>
    root = ET.Element("data")

    # Iterate through the dictionary and add children to the root
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Wrap the root in an ElementTree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a Python dictionary.

    Args:
        filename (str): The name of the input XML file.

    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary from child elements
        # Note: All values will be returned as strings by default
        return {child.tag: child.text for child in root}

    except FileNotFoundError:
        return None
    except Exception:
        return None
