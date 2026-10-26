import json
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from retrieval_baseline import answer, retrieve
DOCS = json.loads((ROOT / 'data' / 'base_conocimiento_demo.json').read_text(encoding='utf-8'))
class RetrievalTests(unittest.TestCase):
    def test_garantia(self):
        self.assertEqual(retrieve('garantía', DOCS)[0]['id'], 'DEMO-001')
    def test_devolucion(self):
        self.assertEqual(retrieve('devolución', DOCS)[0]['id'], 'DEMO-002')
    def test_abstencion(self):
        self.assertEqual(answer('astronomía cuántica', DOCS)['estado'], 'abstencion')
    def test_fuentes(self):
        self.assertTrue(answer('seguimiento pedido', DOCS)['fuentes'])
if __name__ == '__main__':
    unittest.main()
