from py2neo import Graph, Node, Relationship, Subgraph
from py2neo.ext.ogm import Store
from models import Screen, Navigation, Asset

class NeoProvider(object):
	
	def __init__(self):
		
		# TODO read this from a config file
		uri = "http://neo4j:grumble@localhost:7474/db/data"
		self.graph = Graph(uri)
		self.store = Store(self.graph)
		
	def get_start_screen(self):
		# Fetch the start node
		start_node = self.graph.find_one("screen", "start", True)

		# Find all the navigations from the start node
		nav_rels = self.graph.match(start_node, "nav")

		# Find all the assets for the start node
		asset_rels = self.graph.match(start_node, "hasAsset")

		# Construct the DTOs
		assets = [Asset(asset_rel.end_node) for asset_rel in asset_rels]
		navs = [Navigation(nav_rel) for nav_rel in nav_rels]
		start_screen = Screen(start_node, navs, assets)
		return start_screen

	def get_next_screen(self, current_screen_key, option):
		# Fetch the current node
		current_node = self.graph.find_one("screen", "id", current_screen_key)

		# Navigate to the next node via option
		current_rels = self.graph.match(current_node, "nav")
		selected_rel = [rel for rel in current_rels if rel.properties['opt'] == int(option)][0]
		next_node = selected_rel.end_node

		# Grab new navigations and assets for the next node
		next_nav_rels = self.graph.match(next_node, "nav")
		asset_rels = self.graph.match(next_node, "hasAsset")

		# Construct the DTOs
		assets = [Asset(asset_rel.end_node) for asset_rel in asset_rels]
		navs = [Navigation(nav_rel) for nav_rel in next_nav_rels]
		next_screen = Screen(next_node, navs, assets)
		return next_screen
