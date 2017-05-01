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
		start_screen_map = self.graph.cypher.execute("MATCH (q {start: true}) RETURN q").to_subgraph()
		start_screen_node = iter(start_screen_map.nodes).next()
		# start_screen.key = first_question.properties['id']
		# start_screen.question = first_question.properties['text']

		# Grab all nav relationships pointing out of the start node
		relationship_map = self.graph.cypher.execute("MATCH (q {start: true})-[r]->() RETURN q,r").to_subgraph()
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

	# def get_next_screen(self, from_rel):
	# 	next_screen = Screen()
	# 	node_map = self.graph.cypher.execute("MATCH (q {id: %d})-[r]->() RETURN q,r" % from_rel.end_node.properties['id']).to_subgraph()

	# 	next_screen.question = from_rel.end_node
	# 	next_screen.ans1 = next(iter(node_map.relationships), None)
	# 	next_screen.ans2 = from_rel
	# 	next_screen.ans3 = from_rel

	# 	return next_screen
