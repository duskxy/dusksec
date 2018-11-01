import MySQLdb
import sys
import re

class scrim(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='a05370385a',db='dusksec')
        self.cur = self.conn.cursor()
    def sone(self):
        self.cur.execute("select id,url from src")
        self.conn.commit()
        for id,url in self.cur.fetchall():
            yield id,url
    def sint(self,aid,aip,aurl):
        print('insert into asset(suburl,ip,url_id) values("{0}","{1}",{2})'.format(aurl,aip,aid))
        self.cur.execute("insert into asset(suburl,ip,url_id) values('{0}','{1}',{2})".format(aurl,aip,aid))
        self.conn.commit()
    def sfile(self,sfile):
            for x,y in self.sone():
                print(y)
                #rre = re.compile(r"\|(\w*{name})\|(\d+\.){{3}}\d+\|(\d{{1,5}})".format(name=y))
                #rre = re.compile(r"\|\w+({name})\|(.*?)\|(.*?)".format(name=y))
                rre = re.compile(r"\|(.*?{name})\|((\d+?\.){{3}}\d+?)\|(\d{{1,5}})".format(name=y))
                with open(sfile,'r') as f:
                    rres = rre.findall(f.read())
                if rres:
                    print("匹配到:")
                    print("============")
                    for u,p,s,z in rres:
                        print("{}-{}-{}".format(u,p,z))
                        print("入库操作:")
                        self.sint(x,p + ":" + z,u)
                else:
                    print("No match")


    def __del__(self):
        self.cur.close()
        self.conn.close()

if __name__ == "__main__":
    u = scrim()
    u.sfile("dip.txt")
