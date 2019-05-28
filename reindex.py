from elasticsearch import Elasticsearch
import elasticsearch.helpers
elasticDestination = Elasticsearch([{"host": "192.168.86.59", "port": 8240}])
elasticSource = Elasticsearch([{"host": "192.168.86.97", "port": 8240}])
elasticDestination.indices.delete(index="adarshs", ignore=[400, 404])
elasticsearch.helpers.reindex\
    (client=elasticSource, source_index="documents", target_index="adarshs", target_client=elasticDestination)
