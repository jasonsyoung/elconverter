import glob, os, sys
from .helpers import ElementList


class Runner:
    def __init__(self, directory, include_speakers, include_tags):
        self.directory = directory
        self.include_speakers = include_speakers
        self.include_tags = include_tags
        self.element_lists = []
        self.run()

    def run(self):
        json_files = glob.glob(os.path.join(self.directory, "*.json"))
        if len(json_files) is 0:
            print("No JSON files found to convert", file=sys.stderr)
            sys.exit(2)
        for json in json_files:
            with open(json, 'r') as f:
                self.element_lists.append(ElementList(f))

        print("Found {} element list files".format(len(self.element_lists)))
        print(str(self.element_lists[0]))