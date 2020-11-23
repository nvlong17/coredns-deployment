from DatabaseClient import DatabaseConnect
from Ultility import Ultility
from TimeManager import TimeManager
import warnings


class TwitterIOC:
    def __init__(
        self,
        hostURL,
        myDatabase,
    ):
        self.hostURL = hostURL
        self.myDatabase = myDatabase

    # Poll content for AlientVault Taxi Server
    def get_domain_and_insert_database(self):
        Ultility.print_and_write_to_log(
            "-------------------- HOST URL: "
            + self.hostURL
            + "----------------------\n"
        )
        # Ingnore Warning
        warnings.filterwarnings("ignore")
        Ultility.print_and_write_to_log(
            "-------------------- Collection Name: "
            + "Twitter IOC"
            + "----------------------\n"
        )
        blockOfXML = 0
        try:
            blockOfXML += 1
            # Convert XML data to list of domains
            domains = [
                domain
                for domain in Ultility.get_domain_from_text(self.hostURL)
                if Ultility.is_domain_resolveable(domain)
            ]
            # Loop through each domain in the list
            (
                numberOfDomains,
                duplicatedDomains,
            ) = self.myDatabase.load_to_database(domains)
            # Print result to Terminal
            Ultility.print_result(blockOfXML, numberOfDomains, duplicatedDomains)
        except Exception as e:
            Ultility.print_error(blockOfXML, str(e))