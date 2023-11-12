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
        authors = header["authors"]
        deps = header["dependencies"]
        dev_deps = header["group"]["dev"]["dependencies"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(header["name"], header["description"], header["license"], authors,  deps, dev_deps)
