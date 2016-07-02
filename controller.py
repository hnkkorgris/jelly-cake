from py2neo import Graph, Node, Relationship, Subgraph
from py2neo.ext.ogm import Store
from models import Screen

class NeoProvider(object):
	
	def __init__(self):
		
		# TODO read this from a config file
		uri = "http://neo4j:firebird101@localhost:7474/db/data"
		self.graph = Graph(uri)
		self.store = Store(self.graph)
		
	def get_start_screen(self):
		node_map = self.graph.cypher.execute("MATCH (q {asset: 1})-[r]->() RETURN q,r").to_subgraph()
		start_screen = Screen()

		init_node = iter(node_map.nodes).next()
		start_screen.question = init_node

		answers = [None for i in range(3)]
		rel_iterator = iter(node_map.relationships)
		current_rel = next(rel_iterator, None)
		while(current_rel != None):
			answers[current_rel.properties['opt']-1] = current_rel
			current_rel=next(rel_iterator, None)
		start_screen.ans1 = answers[0]
		start_screen.ans2 = answers[1]
		start_screen.ans3 = answers[2]

		return start_screen

	def get_next_screen(self, from_rel):
		next_screen = Screen()
		node_map = self.graph.cypher.execute("MATCH (q {id: %d})-[r]->() RETURN q,r" % from_rel.end_node.properties['id']).to_subgraph()

		next_screen.question = from_rel.end_node
		next_screen.ans1 = next(iter(node_map.relationships), None)
		next_screen.ans2 = from_rel
		next_screen.ans3 = from_rel

		return next_screen