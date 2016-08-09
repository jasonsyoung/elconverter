import os, json
from enum import Enum


class ElementList:
    """ represents an Element List"""
    srt_format = "{}\n{}\n\n"

    def __init__(self, file):
        obj = json.load(file)
        self.version = obj['version']
        self.start_time = obj['start_time']
        self.end_time = obj['end_time']
        self.language = obj['language']
        self.keywords = obj['keywords'] if hasattr(obj, 'keywords') else {}
        self.topics = obj['topics'] if hasattr(obj, 'topics') else {}
        self.entities = obj['entities'] if hasattr(obj, 'entities') else {}
        self.speakers = {}
        for speaker in obj['speakers']:
            speaker = Speaker(speaker)
            self.speakers[speaker.id] = speaker
        self.segments = []
        for segment in obj['segments']:
            self.segments.append(Segment(segment, self.speakers))

    def __str__(self):
        output = ""
        for seq in range(1, len(self.segments) + 1):
            output += ElementList.srt_format.format(seq, self.segments[seq - 1])
        return output


class Segment:
    """ represents a segment"""

    def __init__(self, segment, speakers):
        self.speaker_change = segment['speaker_change']
        self.speaker_id = segment['speaker_id'] if 'speaker_id' in segment else None
        self.interpolated = segment['interpolated'] if 'interpolated' in segment else None
        self.start_time = segment['start_time']
        self.end_time = segment['end_time']
        self.style = segment['style'] if 'style' in segment else None
        speaker = speakers[self.speaker_id] if self.speaker_change else None
        self.sequences = []
        for sequence in segment['sequences']:
            self.sequences.append(Sequence(sequence, speaker))

    def __str__(self):
        return '\n'.join(str(x) for x in self.sequences)


class Sequence:
    """ represents a sequence """

    def __init__(self, sequence, speaker):
        self.interpolated = sequence['interpolated'] if 'interpolated' in sequence else None
        self.start_time = sequence['start_time']
        self.end_time = sequence['end_time']
        self.confidence_score = sequence['confidence_score'] if 'confidence_score' in sequence else None
        self.tokens = []
        self.speaker = '[{}]'.format(speaker) if speaker is not None else ''
        for token in sequence['tokens']:
            self.tokens.append(Token(token))
        self.style = sequence['style'] if 'style' in sequence else None

    def __str__(self):
        start = ms_to_timestamp(self.start_time)
        end = ms_to_timestamp(self.end_time)
        lines = ' '.join(str(x) for x in self.tokens)
        return '{} --> {} {}\n{}'.format(start, end, self.speaker, lines)


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

    def __str__(self):
        return self.display_as



class Speaker:
    """ represents a speaker """

    def __init__(self, speaker):
        self.id = speaker['id']
        self.name = speaker['name']
        self.gender = speaker['gender']




def ms_to_timestamp(ms):
    s, mms = divmod(ms, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)

    return "{}:{}:{},{}".format(h, m, s, mms)