import json
from enum import Enum

class Item:
	def __init__(self, filepath):
		with open(filepath) as json_file:
			data = json.load(json_file)
			self.__dict__ = data
