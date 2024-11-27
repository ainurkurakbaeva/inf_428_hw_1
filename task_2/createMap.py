from elasticsearch import Elasticsearch

# Specify the full connection details with 'scheme', 'host', and 'port'
# es = Elasticsearch(
#     [{'scheme': 'http', 'host': 'localhost', 'port': 9200}]
# )
es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])

# Create index with mappings
def create_index():
    index_name = "threat_scores"
    mapping = {
        "mappings": {
            "properties": {
                "department": {
                    "type": "keyword"
                },
                "threat_scores": {
                    "type": "float"
                }
            }
        }
    }

    # Create the index with mappings
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, body=mapping)
        print(f"Index {index_name} created successfully.")
    else:
        print(f"Index {index_name} already exists.")

# Call to create the index
create_index()
