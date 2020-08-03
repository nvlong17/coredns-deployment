from stix.core import STIXPackage
from lxml import etree
import re
import tldextract

class Ultility:
    #Open a XML file
    @staticmethod
    def openXMLFile(filename):
        file = open(filename, 'r')
        return file.read()

    @staticmethod
    def print_and_write_to_log(strings):
        for string in strings:
            print(string, end="")
        file = open('logs/log_file.txt', "a")
        file.writelines(strings)
        file.close()

    #Print Result
    @staticmethod
    def print_result(blockOfXML,numberOfDomains,duplicatedDomains):
        strings = ['---------------------- Block of XML Processed: ' + str(blockOfXML) + ' -----------------------\n',
                   'Number of INSERTED domains: ' + str(numberOfDomains) + '\n',
                   'Number of DUPLICATED domains: ' + str(duplicatedDomains) + '\n',
                   '----------------------------------------------------------------------------\n']
        Ultility.print_and_write_to_log(strings)
        
    @staticmethod
    def print_error(blockOfXML,exception):
        strings = ['---------------------- Block of XML Processed: '+str(blockOfXML)+' -----------------------\n',
                   'ERROR: '+ exception+"\n",
                   "THIS BLOCK TERMINATED"+"\n",
                   '----------------------------------------------------------------------------'+'\n']
        Ultility.print_and_write_to_log(strings)

    @staticmethod
    def get_converted_domain(rawDomain):
        address = tldextract.extract(rawDomain)
        #Remove case IPv4 URL (http://192.169.0.1/) Regex: ^ for begining, d+ for any number, \. for .
        if not re.match("^\d+\.\d+\.\d+\.\d+",address.domain):
            return address.domain + '.' + address.suffix
        else:
            return None

    @staticmethod
    def is_acceptable_data_type(dataType):
        #Check type of XML
        acceptableDataType = ['URIObjectType', 'DomainNameObjectType']
        if (dataType in acceptableDataType):
            return True
        return False

    @staticmethod
    def get_domain_from_XML(XMLData,hostURL,collectionName):
        #Conevert XML to STIX Object -> dictionary
        stixPackage = STIXPackage.from_xml(etree.fromstring(XMLData))
        stixDict = stixPackage.to_dict()
        
        domains = []
        #Check XML block type, Specific for ei.botnet XML block due to differences
        if (collectionName=='ei.botnet'):
            #Loop through every observable tag
            for observable in stixDict['observables']['observables']:
                #Loop through every related object tag
                for relateObj in observable['object']['related_objects']:
                    if Ultility.is_acceptable_data_type(relateObj['properties']['xsi:type']):
                        rawDomain = relateObj['properties']['value']
                        domain = Ultility.get_converted_domain(rawDomain)
                        if domain is not None:
                            domains.append(domain)
        else:    
            #Loop through every Indicator Tag
            for indicator in stixDict['indicators']:
                dataType = indicator['observable']['object']['properties']['xsi:type']
                #Check data can be converted to domain or not?
                if Ultility.is_acceptable_data_type(dataType):
                    rawDomain = indicator['observable']['object']['properties']['value']
                    # eti.eset.com has domain nested in another tag
                    if (hostURL=='eti.eset.com'):
                        rawDomain = rawDomain['value']
                    domain = Ultility.get_converted_domain(rawDomain)
                    if domain is not None:
                        domains.append(domain)
        #Remove Duplicated Domains
        domains = list(dict.fromkeys(domains))
        return domains
