import glob, os, sys, zipfile
from .helpers import ElementList

"""

runner.py

This runs the conversion

"""


class Runner:
    def __init__(self, directory, include_speakers, include_tags):
        self.directory = directory
        self.include_speakers = include_speakers
        self.include_tags = include_tags

    def run(self):
        json_files = glob.glob(os.path.join(self.directory, "*.json"))
        if len(json_files) is 0:
            print("No JSON files found to convert", file=sys.stderr)
            return False

        files = []
        for json in json_files:
            with open(json, 'r') as f:
                el = ElementList(f)
            with open(os.path.splitext(json)[0] + '.srt', 'w') as f:
                f.write(el.to_srt(self.include_speakers, self.include_tags))
                files.append(f.name)

        if len(files) > 1:
            with zipfile.ZipFile(self.directory + '.zip', 'w', zipfile.ZIP_DEFLATED) as zfile:
                for f in files:
                    zfile.write(f, os.path.basename(f))
                    os.remove(f)
            print("Wrote {} files to {}".format(len(files), self.directory + '.zip'))
        else:
            print("Created {}".format(files[0]))
