import os
import sys
import json
import time

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

from uasparser2 import UASParser

test_uas = json.load(open('test/uas.json', 'r'))

t0 = time.time()
up = UASParser(mem_cache_size=100)
print ('load:', time.time() - t0)

t0 = time.time()
for uas, obj in test_uas:
    try:
        new_obj = up.parse(uas)

        assert new_obj == obj
    except Exception:
        print(uas)
        for k in set(new_obj.keys()) | set(obj.keys()):
            if obj.get(k) != new_obj.get(k):
                print(k, obj.get(k, '').encode('utf-8'), new_obj.get(k, '').encode('utf-8'))

print()
print ('parse:', time.time() - t0)
