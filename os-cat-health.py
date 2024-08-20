from opensearchpy import OpenSearch
import json

host = 'localhost'
port = 9200
auth = ('admin', 'admin') # For testing only. Don't store credentials in code.

# Create the client with SSL/TLS enabled, but hostname verification disabled.
client = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_compress = True,
    http_auth = auth,
    use_ssl = True,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False,
)

index_name = '*'

response = client.cat.indices(
    index = index_name,
    v = True,
    s = 'index',
)

print(response)