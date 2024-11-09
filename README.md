# fluent-bit

```bash

for i in {1..100}; do curl -d '{"log_group":"555555","key2":"value2"}' -XPOST -H "content-type: application/json" http://localhost:8888/logs.test; done
for i in {1..100}; do curl -d '{"log_group":"lololol","log":"[AUDIT] test message"}' -XPOST -H "content-type: application/json" http://localhost:8888/logs.test; done

curl -X POST -d '{}' localhost:2020/api/v2/reload


docker compose down fluent-bit; docker compose up -d; docker logs fluent-bit -f
```