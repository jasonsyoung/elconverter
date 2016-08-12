import json


class ElementList:
    """ represents an Element List"""

    def __init__(self, file):
        obj = json.load(file)
        self.start_time = obj['start_time']
        self.end_time = obj['end_time']
        self.speakers = {}
        for speaker in obj['speakers']:
            speaker = Speaker(speaker)
            self.speakers[speaker.id] = speaker
        self.segments = []
        for segment in obj['segments']:
            self.segments.append(Segment(segment, self.speakers))

    def to_srt(self, include_speakers, include_tags):
        subtitles = ''
        index = 1
        for a, b in enumerate(x.to_list(include_speakers, include_tags) for x in self.segments):
            for c in b:
                subtitles += '{}\n{}\n\n'.format(index, c)
                index += 1
        return subtitles


class Segment:
    """ represents a segment"""
    LINE_LENGTH = 32

    def __init__(self, segment, speakers):
        self.speaker_change = segment['speaker_change']
        self.speaker_id = segment['speaker_id'] if 'speaker_id' in segment else None
        self.start_time = segment['start_time']
        self.speaker = speakers[self.speaker_id].name if self.speaker_change else None
        self.sequences = []
        for sequence in segment['sequences']:
            self.sequences.append(Sequence(sequence))

    def to_list(self, include_speakers, include_tags):
        blocks = []
        line = ''
        lines = []
        start = self.start_time
        for i, s in enumerate(self.sequences):
            if include_speakers and i == 0 and self.speaker_change:
                line = '[{}] '.format(self.speaker)
            for t in s.tokens:
                if start is None:
                    start = t.start_time

                next_token = str(t)
                if include_tags and len(t.tags) > 0 and t.tags[0] != Token.TYPE_END_SENTENCE:
                    next_token = '[{}] {}'.format(t.tags[0], str(t))

                if t.type != Token.TYPE_PUNCTUATION and len(line) + len(next_token) > Segment.LINE_LENGTH:
                    if len(lines) == 0:
                        lines.append(line.lstrip())
                        line = ''
                    else:
                        lines.append(line.lstrip())
                        blocks.append(SRT(start, end, lines))
                        start = None
                        lines = []
                        line = ''

                if t.type == 'punctuation':
                    line = line.rstrip() + next_token
                elif len(line) == 0:
                    line += next_token
                else:
                    line += ' {}'.format(next_token)

                end = t.end_time

        lines.append(line.lstrip())
        blocks.append(SRT(start, end, lines))

        return map(lambda x: str(x), blocks)


class SRT:
    def __init__(self, start, end, lines):
        self.start = ms_to_timestamp(start)
        self.end = ms_to_timestamp(end)
        self.lines = lines

    def __str__(self):
        return '{} --> {}\n{}'.format(self.start, self.end, '\n'.join(self.lines))


class Sequence:
    """ represents a sequence """

    def __init__(self, sequence):
        self.interpolated = sequence['interpolated'] if 'interpolated' in sequence else None
        self.start_time = sequence['start_time']
        self.end_time = sequence['end_time']
        self.confidence_score = sequence['confidence_score'] if 'confidence_score' in sequence else None
        self.tokens = []
        for token in sequence['tokens']:
            self.tokens.append(Token(token))
        self.style = sequence['style'] if 'style' in sequence else None


class Token:
    """ represents a token """

    TYPE_PUNCTUATION = 'punctuation'
    TYPE_END_SENTENCE = 'ENDS_SENTENCE'


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
        return self.display_as if len(self.display_as) > 0 else self.value



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