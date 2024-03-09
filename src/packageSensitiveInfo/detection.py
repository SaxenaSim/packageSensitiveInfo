import logging , re
import sys,os

logging.basicConfig(filename="logs/myLogs.log",level=logging.DEBUG,format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        
class detection:
    def __init__(self):
        self.contents=""
        self.patterns=[]
        self.logger = logging.getLogger()
    
    def read_data_file(self,file):
        logging.debug("::Entering into read_data_file_method::")
        with open(file,'r') as f:
            self.contents = f.read()
            self.logger.debug(self.contents)

    def read_regex_file(self,file):
        logging.debug("::Entering into read_regex_method::")
        with open(file,'r') as f:
            self.logger.debug(self.patterns)
            self.patterns = f.read().split(',')
            
    def find_matches(self):
        self.logger.debug("::: find_matches :::")
        #logging.debug(patterns)
        for i in self.patterns:
            self.logger.debug("::: i = :::")
            self.logger.debug(i)
            if re.search(i,self.contents,flags=re.IGNORECASE):
                self.logger.debug("::: inside IF :::")    
            else:
                self.logger.debug("::: no match found:::")
                self.logger.debug(i)

if __name__=="__main__":
    
    ptrn_file="data/patterns.txt"   
    data_file="data/data.txt"   

    data_file_name=input("Enter Data File Name : ")
    ptrn_file_name=input("Enter Pattern File Name : ")
    

    if (data_file_name != ""):
        data_file="data/"+data_file_name
        
    if (ptrn_file_name != ""):
        ptrn_file="data/"+ptrn_file_name
    
    objDetection = detection()
    pkgLogger = logging.getLogger()
    
    pkgLogger.debug("::data_file::")
    pkgLogger.debug(data_file)
    pkgLogger.debug("::ptrn_file_name::")
    pkgLogger.debug(ptrn_file)
    
    
    objDetection.read_data_file(data_file)
    objDetection.read_regex_file(ptrn_file)
    objDetection.find_matches()