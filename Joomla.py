from CMS import CMS
from PrintUtils import print_debug

# This class represents a Joomla installation
class Joomla(CMS):

    def __init__(self, path):
        super().__init__(path)


    def compare_with_clean_installation(self):
        pass

    def get_version(self):
        pass

    def download_clean_installation(self):
        pass

    def search_suspect_files(self):
        results = []

        return results

    def search_suspect_content(self):
        results = []

        return results


    def search_malware_signatures(self):
        results = []

        return results