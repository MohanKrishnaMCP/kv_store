from kv_store import KeyValueStore
from persistence import PersistentKeyValueStore

def test_set_get():
    kv = KeyValueStore()
    kv.setval('foo', 'bar')
    assert kv.get('foo') == 'bar'
    assert kv.get('baz') == None

def test_persistence():
    kv = PersistentKeyValueStore('test_db.json')
    kv.setval('foo', 'bar')
    kv = PersistentKeyValueStore('test_db.json')
    assert kv.get('foo') == 'bar'
    kv.delete('foo')
    kv = PersistentKeyValueStore('test_db.json')
    assert kv.get('foo') == None
    import os
    os.remove('test_db.json')

test_set_get()
test_persistence()