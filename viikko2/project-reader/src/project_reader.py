from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed_data = toml.loads(content)
        header = parsed_data["tool"]["poetry"]
        dependencies = parsed_data["tool"]["poetry"]["dependencies"]
        dev_dependencies = parsed_data["tool"]["poetry"]["group"]["dev"]["dependencies"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(header["name"], header["description"], dependencies, dev_dependencies)
