# Override LaTeXTranslator to style the first paragraph of
# field list definitions.

from docutils import nodes
from sphinx.writers.latex import LaTeXTranslator

def my_visit_paragraph(self, node):
   self._visit_paragraph(node)

   index = node.parent.index(node)
   if (index == 0 and isinstance(node.parent, nodes.field_body)):
      self.body.append("\\DUrole{fieldlistfirstparagraph}{")

def my_depart_paragraph(self, node):
   index = node.parent.index(node)
   if (index == 0 and isinstance(node.parent, nodes.field_body)):
      self.body.append("}")

   self._depart_paragraph(node)

LaTeXTranslator._visit_paragraph = LaTeXTranslator.visit_paragraph
LaTeXTranslator.visit_paragraph = my_visit_paragraph

LaTeXTranslator._depart_paragraph = LaTeXTranslator.depart_paragraph
LaTeXTranslator.depart_paragraph = my_depart_paragraph

def setup(app):
   pass
