# fluent-bit

for i in {1..100}; do curl -d '{"log_group":"555555","key2":"value2"}' -XPOST -H "content-type: application/json" http://localhost:8888/logs.test; done
curl -X POST -d '{}' localhost:2020/api/v2/reload