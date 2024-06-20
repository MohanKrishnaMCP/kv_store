from kv_store import KeyValueStore

kv_store = KeyValueStore()
print(kv_store.set('name', 'Alice'))  # True
print(kv_store.get('name'))  # Alice
print(kv_store.delete('name'))  # True
print(kv_store.get('name'))  # None
print(kv_store.exists('name'))  # False
print(kv_store.set('age', 30))  # True
print(kv_store.get('age'))  # 30
print(kv_store.clear())  # True
print(kv_store.get('age'))  # None