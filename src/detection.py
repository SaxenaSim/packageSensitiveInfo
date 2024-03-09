import logging , re
import sys

logging.basicConfig(filename="logs/myLogs.log",level=logging.DEBUG,format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        
class detection:
    def __init__(self):
        self.contents=""
        self.patterns=[]
        self.logger = logging.getLogger()
        self.ptrn_file="data/patterns.txt"   
        self.data_file="data/data.txt"   

    
    def read_data_file(self,file):
        try:
            logging.debug("::Entering into read_data_file_method::")
            logging.debug(file)
            if (file != ""):
                self.data_file="data/"+ file
        
            with open(self.data_file,'r') as f:
                self.contents = f.read()
                self.logger.debug(self.contents)
            
            return self.data_file
        except Exception as e:
            logging.debug("::Data Exception::")
            logging.error(e)
            return None

    def read_regex_file(self,file):
        try:
            logging.debug("::Entering into read_regex_method::")
            logging.debug(file)
            if (file != ""):
                self.ptrn_file="data/"+file
    
            with open(self.ptrn_file,'r') as f:
                self.logger.debug(self.patterns)
                self.patterns = f.read().split(',')
                
            return self.ptrn_file
        except Exception as e:
            logging.debug("::RegEx Exception::")
            logging.error(e)
            return None
            
    def find_matches(self):
        try:
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
            return True
        except Exception as e:
            logging.debug("::Exception::")
            logging.error(e)
            return False

if __name__=="__main__":
    
    data_file_name=input("Enter Data File Name : ")
    ptrn_file_name=input("Enter Pattern File Name : ")
    
    objDetection = detection()
    
    objDetection.read_data_file(data_file_name)
    objDetection.read_regex_file(ptrn_file_name)
    objDetection.find_matches()
    
    
    
