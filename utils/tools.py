import subprocess
import os
# python dirsearch/dirsearch.py -u www.2345.com -e * --plain-text-report=2345

class Ctools:
    ct = os.path.dirname(os.path.abspath(__file__)) 
    sub = "extra/Sublist3r/sublist3r.py -d "
    dsub = "extra/dirsearch/dirsearch.py -u {0} -e * --plain-text-report={1}/dircom/{2}.txt"
    dir = ""
    data = list()
    ddata = list()
    def domain(self,udomain,surl,sudata):
        result = subprocess.Popen(self.ct + "/" + self.sub + udomain +" -o " + self.ct + "/subcom/" + udomain + ".txt",stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
        while 1:
            out = result.stdout.readline().decode("utf-8")
            print(result.stdout.readline().decode("utf-8"))
            if out == "":
                su = surl(url=udomain)
                su.save()
                with open(self.ct + "/subcom/" + udomain + ".txt",'r') as ff:
                    for i in ff.readlines():
                        ii = i.strip()
                        sd = sudata(url=ii,uid_id=su.id)
                        sd.save()
                        self.data.append(ii)
                break
        return self.data
    def dodir(self,domain):
        print(self.ct + "/" + self.dsub.format(domain,self.ct,domain))
        dsult = subprocess.Popen(self.ct + "/" + self.dsub.format(domain,self.ct,domain),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
        while 1:
            dout = dsult.stdout.readline().decode("utf-8")
            print(dsult.stdout.readline().decode("utf-8"))
            if dout == '':
                with open(self.ct + "/dircom/" + domain + ".txt",'r') as df:
                    for di in df.readlines():
                        self.ddata.append(di)
                break
        return self.ddata     
