import json
from Utilities import bcolors

class Item:
	def __init__(self, filepath):
		with open(filepath) as json_file:
			data = json.load(json_file)
			self.__dict__ = data
			self.filepath = filepath

	def __str__(self): # pretty
		return self.title

	def setPosted(self):
		self.__dict__["posted"] = "true"
		with open(self.filepath, "w") as output:
			json.dump(self.__dict__, output)
			