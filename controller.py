from py2neo import Graph, Node, Relationship, Subgraph
from py2neo.ext.ogm import Store
from models import Screen, Navigation

class NeoProvider(object):
	
	def __init__(self):
		
		# TODO read this from a config file
		uri = "http://neo4j:grumble@localhost:7474/db/data"
		self.graph = Graph(uri)
		self.store = Store(self.graph)
		
	def get_start_screen(self):
		# Grab the node with start flag set to mark the beginning of the tree
		start_screen_map = self.graph.cypher.execute("MATCH (n {start: true}) RETURN n").to_subgraph()
		start_screen_node = iter(start_screen_map.nodes).next()

		# Grab all nav relationships pointing out of the start node
		relationship_map = self.graph.cypher.execute("MATCH (n {start: true})-[r]->() RETURN n,r").to_subgraph()
		start_screen_rels = iter(relationship_map.relationships)

		# Construct the navigation objects
		start_screen_navs = []
		current_rel = next(start_screen_rels, None)
		while(current_rel != None):
			start_screen_navs.append(Navigation(current_rel))
			current_rel = next(start_screen_rels, None)

		# Construct the start screen
		start_screen = Screen(start_screen_node, start_screen_navs)
		return start_screen

	# TODO lots of duplciate code, rework a bit
	def get_next_screen(self, current_screen_key, option):
		# Grab the node that option points to from current_screen
		query = "MATCH (:screen {id: %s})-[:nav {opt: %s}]->(n:screen) RETURN n" % (current_screen_key, option)
		node_map = self.graph.cypher.execute(query).to_subgraph()
		node = iter(node_map.nodes).next()

		# Grab the relationships
		query = "MATCH (:screen {id: %d})-[r:nav]->() RETURN r" % node.properties['id']
		relationship_map = self.graph.cypher.execute(query).to_subgraph()
		rels = iter(relationship_map.relationships)

		# Construct the navigation objects
		next_screen_navs = []
		current_rel = next(rels, None)
		while(current_rel != None):
			next_screen_navs.append(Navigation(current_rel))
			current_rel = next(rels, None)
		
		# Construct the screen
		next_screen = Screen(node, next_screen_navs)
		return next_screen
