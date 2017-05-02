class Screen(object):
	
	def __init__(self, node, navs=None, assets=None):
		self.key = node.properties["id"]
		self.text = node.properties["text"]
		# TODO: order navs by option
		self.navs = navs
		self.assets = assets

	def serialize(self):
		return {
			'key': self.key,
			'text': self.text,
			'navs': [nav.serialize() for nav in self.navs],
			'assets': [asset.serialize() for asset in self.assets]
		}

class Navigation(object):

	def __init__(self, rel):
		self.text = rel.properties["text"]
		self.option = rel.properties["opt"]

	def serialize(self):
		return {
			'text': self.text,
			'option': self.option
		}

class Asset(object):

	def __init__(self, node, rel=None):
		self.type = node.properties["type"]
		self.path = node.properties["path"]
		self.pos = "" if rel == None else rel.properties["pos"]

	def serialize(self):
		return {
			'type': self.type,
			'path': self.path,
			'pos': self.pos
		}