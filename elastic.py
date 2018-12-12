import os
from elasticsearch import Elasticsearch

es_port = 9200
es = Elasticsearch('http://127.0.0.1:{0}'.format(es_port)) # Use HTTP
try:
    es.indices.delete(index="test-index")
except:
    pass

es.indices.create(index="test-index")

mapping = {
    'parsedtext': {
        'boost': 1.0,
        'index': True,
        'store': True,
        'type': 'text',
        "term_vector": "with_positions_offsets"
    },
    'name': {
        'boost': 1.0,
        'index': True,
        'store': True,
        'type': 'text',
        "term_vector": "with_positions_offsets"
    },
    'title': {
        'boost': 1.0,
        'index': True,
        'store': True,
        'type': 'text',
        "term_vector": "with_positions_offsets"
    },
    'pos': {
        'store': True,
        'type': 'integer'
    },
    'uuid': {
        'boost': 1.0,
        'index': False,
        'store': True,
        'type': 'keyword'
    }
}
es.indices.put_mapping(doc_type="test-type", body={"properties": mapping}, index="test-index")

es.index(index="test-index", doc_type="test-type", id=1, body={"name":"Joe Tester", "parsedtext":"Joe Testere nice guy", "uuid":"11111", "position":1})
es.index(index="test-index", doc_type="test-type", id=2, body={"name":"Bill Baloney", "parsedtext":"Joe Testere nice guy", "uuid":"22222", "position":2})

es.indices.refresh(index="test-index")

results = es.search(index="test-index", body={"query": {"match": {"name": "joe"}}})

for r in results['hits']['hits']:
   print(r)
