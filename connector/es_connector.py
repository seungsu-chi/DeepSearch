from .config import es_config 
from elasticsearch import Elasticsearch
import json

class ES:
    
    es = Elasticsearch(hosts = es_config.hosts, http_auth=es_config.auth)
    
    @classmethod
    def srvHealthCheck(cls):
        health = cls.es.cluster.health()
        print (health)

    @classmethod
    def allIndex(cls):
        # Elasticsearch에 있는 모든 Index 조회
        print (cls.es.cat.indices())

    @classmethod
    def dataInsert(cls,index,data):
        # ===============
        # 데이터 삽입
        # ===============
        
        res = cls.es.index(index=index, body=data)
        print (res)

    @classmethod
    def searchAll(cls, indx=None):
        # ===============
        # 데이터 조회 [전체]
        # ===============
        res = cls.es.search(
            index = indx,
            body = {
                "query":{"match_all":{}}
            }
        )
        print (json.dumps(res, ensure_ascii=False, indent=4))

    @classmethod
    def searchFilter(cls,index,body):
        # ===============
        # 데이터 조회 []
        # ===============
        res = cls.es.search(
            index = index,
            body = body
        )
        ppr.pprint(res)

    @classmethod
    def createIndex(cls,index,body=None):
        # ===============
        # 인덱스 생성
        # ===============
        cls.es.indices.create(
            index = index,
            body = body
        )
        
    @classmethod
    def deleteIndex(cls,index):
        cls.es.indices.delete(
            index = index
        )