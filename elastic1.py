from elasticsearch import Elasticsearch
def showAll():
    try:
        res = es.search(index="empindex", body={"query": {"match_all": {}}})
        for i in res["hits"]["hits"]:
            record = i["_source"]
            print("************")
            print("ID : "+i["_id"])
            print("Firstname : "+record["firstname"])
            print("Lastname : "+record["lastname"])
            print("age : "+record["age"])
            print("************")
        raw_input()
    except:
        print("Something went wrong..!!")
def searchRecord():
    try:
        print("Enter firstname : ")
        firstname=raw_input()
        res=es.search(index="empindex",body={"query":{"match":{"firstname":firstname}}})
        for i in res["hits"]["hits"]:
            record = i["_source"]
            print("************")
            print("ID : "+i["_id"])
            print("Firstname : "+record["firstname"])
            print("Lastname : "+record["lastname"])
            print("age : "+record["age"])
            print("************")
        raw_input()
    except:
        print("Something went wrong..!!")
def enterData():
    print("Enter ID : ")
    empid=raw_input()
    print("Enter firstname : ")
    firstname=raw_input()
    print("Enter lastname : ")
    lastname=raw_input()
    print("Enter age : ")
    age=raw_input()
    empbody={"firstname":firstname,"lastname":lastname,"age":age}
    res=es.index(index="empindex",doc_type="emp",id=empid,body=empbody)
    print(res["result"])
    raw_input()
def showData():
    print("Enter 1 for Display all records\nEnter 2 search for specific record:")
    print("Enter choice:")
    choice=raw_input()
    if(choice=="1"):
        showAll()
    elif(choice=="2"):
        searchRecord()
def updateData():
    print("Enter ID : ")
    empid=int(raw_input())
    print("Enter firstname : ")
    firstname=raw_input()
    print("Enter lastname : ")
    lastname=raw_input()
    print("Enter age : ")
    age=raw_input()
    empbody={"firstname":firstname,"lastname":lastname,"age":age}
    res=es.index(index="empindex",doc_type="emp",id=empid,body=empbody)
    print(res["result"])
    raw_input()
def deleteData():
    print("Enter ID : ")
    empid=int(raw_input())
    res=es.delete(index="empindex",doc_type="emp",id=empid)
    print(res["result"])
    raw_input()
es=Elasticsearch()
while(True):
    print("**Menu**")
    print("Enter 1 for entering data:")
    print("Enter 2 for show data:")
    print("Enter 3 for update data:")
    print("Enter 4 for delete data:")
    print("Enter 0 for exit:")
    print("Enter choice:")
    choice=raw_input()
    if(choice == "1"):
        enterData()
    elif(choice == "2"):
        showData()
    elif(choice == "3"):
        updateData()
    elif(choice == "4"):
        deleteData()
    elif(choice == "0"):
        exit(0)
