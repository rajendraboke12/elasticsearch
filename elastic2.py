from elasticsearch import Elasticsearch
es=Elasticsearch([{"host":"192.168.86.59","port":8240}])
for i in range(1,51):
    fname="abc"+str(i)
    lname="xyz"+str(i)
    authorbody={"author":"Rajendra","firstname":fname,"lastname":lname,"age":21}
    res=es.index(index="authorindex",doc_type="author",id=i,body=authorbody)
res = es.search(index="authorindex", body={"size":50,"query": {"match_all":  {}}})
print(res)
