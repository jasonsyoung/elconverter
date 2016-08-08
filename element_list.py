import os, json
from enum import Enum

class ElementList:
    """ represents an Element List"""
    srt_format = "{seq}\n{start_time} --> {end_time}\n{lines}\n\n"

    def __init__(self, file):
        obj = json.load(file)
        self.version = obj['version']
        self.start_time = obj['start_time']
        self.end_time = obj['end_time']
        self.language = obj['language']
        self.segments = []
        for segment in obj['segments']:
            self.segments.append(Segment(segment))
        self.keywords = obj['keywords'] if hasattr(obj, 'keywords') else {}
        self.topics = obj['topics'] if hasattr(obj, 'topics') else {}
        self.entities = obj['entities'] if hasattr(obj, 'entities') else {}
        self.speakers = []
        for speaker in obj['speakers']:
            self.speakers.append(Speaker(speaker))

    def to_srt(self):
        output = ""
        for seq in range(0, len(self.segments)):
            output += ElementList.srt_format.format(self.segments[seq])


    def __str__(self):
        string = "version = {}\nstart_time = {}\nend_time = {}\nlanguage = {}\n"
        string += "segments = {}\nkeywords = {}\ntopics = {}\nentities = {}\nspeakers = {}"
        return string.format(self.version, self.start_time, self.end_time, self.language,
                             self.segments, self.keywords,self.topics, self.entities,
                             self.speakers)

class Gender(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    UNKNOWN = "UNKNOWN"


class Speaker:
    """ represents a speaker """

    def __init__(self, speaker):
        self.id = speaker['id']
        self.name = speaker['name']
        self.gender = Gender[speaker['gender']]

    def __str__(self):
        return "id: {}\nname: {}\ngender: {}".format(self.id, self.name, self.gender)

class Segment:
    """ represents a segment"""

    def __init__(self, segment):
        self.speaker_change = segment['speaker_change']
        self.speaker_id = segment['speaker_id'] if 'speaker_id' in segment else None
        self.interpolated = segment['interpolated'] if 'interpolated' in segment else None
        self.start_time = segment['start_time']
        self.end_time = segment['end_time']
        self.style = segment['style'] if 'style' in segment else None
        self.sequences = []
        for sequence in segment['sequences']:
            self.sequences.append(Sequence(sequence))


class Sequence:
    """ represents a sequence """

    def __init__(self, sequence):
        self.name = sequence['name']
        self.start_time = sequence['start_time']
        self.end_time = sequence['end_time']
        self.confidence_score = sequence['confidence_score'] if 'confidence_score' in sequence else None
        self.tokens = []
        for token in sequence['tokens']:
            self.tokens.append(Token(token))
        self.style = sequence['style'] if 'style' in sequence else None


class Token:
    """ represents a token """

    def __init__(self, token):
        self.interpolated = token['interpolated']
        self.start_time = token['start_time']
        self.end_time = token['end_time']
        self.value = token['value']
        self.type = token['type']
        self.display_as = token['display_as']
        self.tags = token['tags']
        self.style = token['style'] if 'style' in token else None
