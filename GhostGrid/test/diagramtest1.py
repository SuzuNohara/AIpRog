from graphviz import Digraph

dot = Digraph()
dot.node('A')
dot.node('B')
dot.edge('A', 'B')
dot.edge('B', 'A')
dot.edge('A', 'C')
dot.edge('B', 'D')
dot.edge('C', 'D')

dot.render('graph', format='png', view=True)
