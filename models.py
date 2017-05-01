class Screen(object):
	
	def __init__(self, node, rels=None):
		self.key = node.properties["id"]
		self.text = node.properties["text"]
		# TODO: order navs by option
		self.navs = rels

	def serialize(self):
		return {
			'key': self.key,
			'text': self.text,
			'navs': [nav.serialize() for nav in self.navs]
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