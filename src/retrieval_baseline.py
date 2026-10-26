"""Baseline académico de recuperación léxica. NO es un sistema RAG productivo."""
import json
import re
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / 'data' / 'base_conocimiento_demo.json'
STOP = {'que','para','con','los','las','una','uno','del','por','como','esta','este','necesito','quiero','sobre','puedo','hacer','tengo','cuál','cual'}

def tokens(text):
    return {x for x in re.findall(r'\w+', text.lower()) if len(x) > 2 and x not in STOP}

def retrieve(question, documents, min_overlap=1):
    q = tokens(question)
    results = []
    for doc in documents:
        score = len(q & tokens(doc['titulo'] + ' ' + doc['contenido']))
        if score >= min_overlap:
            results.append((score, doc))
    results.sort(key=lambda item: (-item[0], item[1]['id']))
    return [doc for _, doc in results]

def answer(question, documents):
    hits = retrieve(question, documents)
    if not hits:
        return {'estado': 'abstencion', 'mensaje': 'No tengo información suficiente. Solicita atención humana.', 'fuentes': []}
    return {'estado': 'recuperacion', 'mensaje': 'Se encontró documentación ilustrativa. Verifica su vigencia antes de responder.', 'fuentes': [d['id'] for d in hits[:3]]}

if __name__ == '__main__':
    docs = json.loads(DATA.read_text(encoding='utf-8'))
    print(json.dumps(answer(' '.join(sys.argv[1:]) or 'garantía', docs), ensure_ascii=False, indent=2))
