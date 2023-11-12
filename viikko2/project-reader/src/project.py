class Project:
    def __init__(self, name, description, proj_license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.proj_license = proj_license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        SEPARATOR = "\n- "
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.proj_license or '-'}"
            f"\n"
            f"\nAuthors:"
            f"\n- {SEPARATOR.join(self.authors)}"
            f"\n"
            f"\nDependencies:"
            f"\n- {SEPARATOR.join(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies:"
            f"\n- {SEPARATOR.join(self.dev_dependencies)}"
        )
