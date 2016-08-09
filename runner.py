import glob, os
from element_list import ElementList


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
            raise "No JSON files found to convert"
        for json in json_files:
            with open(json, 'r') as f:
                self.element_lists.append(ElementList(f))

        print("Found {} element list files".format(len(self.element_lists)))
        print(str(self.element_lists[0]))