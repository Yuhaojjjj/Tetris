import json
import Griders
import pygame
import numpy as np

def getSettings():
    with open("settings.json", "r") as f:
        settings = json.load(f)
        return settings

def getColor(value: int, rgbList: list[list]) -> list:
    """return the RGB color depending on the cell value"""
    return(rgbList[value])