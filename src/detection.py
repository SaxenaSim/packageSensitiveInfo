import logging, re
import sys

logging.basicConfig(
    filename="logs/myLogs.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class detection:
    def __init__(self):
        self.contents = ""
        self.patterns = []
        self.logger = logging.getLogger()
        self.ptrn_file = "data/patterns.txt"
        self.data_file = "data/data.txt"

    """
    Reads the contents of a data file specified by 'file' parameter.
    Constructs the file path, opens the file, reads its contents,
    logs debug messages, and handles any exceptions that may occur.
    
    Parameters:
        file (str): The name of the data file to be read.
        
    Returns:
        str or None: The path to the data file if successful, None otherwise.
    """

    def read_data_file(self, file):
        try:
            logging.debug("::Entering into read_data_file_method::")
            logging.debug(file)
            if file != "":
                self.data_file = "data/" + file

            with open(self.data_file, "r") as f:
                self.contents = f.read()
                self.logger.debug(self.contents)

            return self.data_file
        except Exception as e:
            logging.debug("::Data Exception::")
            logging.error(e)
            return None

    """method to read the file for given input filename.
     If not entered any file it will take the default filename as patterns.txt"""

    def read_regex_file(self, file):
        try:
            logging.debug("::Entering into read_regex_method::")
            logging.debug(file)
            if file != "":
                self.ptrn_file = "data/" + file

            with open(self.ptrn_file, "r") as f:
                self.logger.debug(self.patterns)
                self.patterns = f.read().split(",")

            return self.ptrn_file
        except Exception as e:
            logging.debug("::RegEx Exception::")
            logging.error(e)
            return None

    # method to iterate over the patterns which are taken from read_regex_file() method.
    def find_matches(self):
        try:
            self.logger.debug("::: find_matches :::")
            for i in self.patterns:
                self.logger.debug("::: i = :::")
                self.logger.debug(i)
                return_value = self.regex_match(i, self.contents)
        except Exception as e:
            logging.debug("::Exception::")
            logging.error(e)
            return False

        return return_value

    # method to match the regex pattern to the data which is given in input.
    def regex_match(self, pattern, data):
        if re.search(pattern, data, flags=re.IGNORECASE):
            self.logger.debug("::: inside IF :::")
            return True
        else:
            self.logger.debug("::: no match found:::")
            return False


if __name__ == "__main__":

    data_file_name = input("Enter Data File Name : ")
    ptrn_file_name = input("Enter Pattern File Name : ")

    objDetection = detection()

    objDetection.read_data_file(data_file_name)
    objDetection.read_regex_file(ptrn_file_name)
    objDetection.find_matches()
