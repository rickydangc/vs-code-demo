from pymilvus import connections

connections.connect(
    user="",
    password="",
    alias="default",
    host="milvus-np0.azure.wus2.walmart.com",
    port="31480"
)