import unittest

json = """{
  "speakers": [
    {
      "gender": "Female",
      "name": "Test Speaker",
      "id": 0
    }
  ],
  "language": "en",
  "start_time": 5590,
  "version": 3,
  "end_time": 351910,
  "segments": [
    {
      "start_time": 5590,
      "interpolated": true,
      "speaker_change": true,
      "end_time": 6590,
      "sequences": [
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 5590,
              "tags": [],
              "value": "so",
              "display_as": "So",
              "end_time": 5910,
              "type": "word"
            }
          ],
          "start_time": 5590,
          "end_time": 5910,
          "confidence_score": 0.227
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 5910,
              "tags": [],
              "value": "welcome",
              "display_as": "welcome",
              "end_time": 6130,
              "type": "word"
            }
          ],
          "start_time": 5910,
          "end_time": 6130,
          "confidence_score": 0.97
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 6130,
              "tags": [],
              "value": "back",
              "display_as": "back",
              "end_time": 6430,
              "type": "word"
            },
            {
              "interpolated": false,
              "start_time": 6430,
              "tags": [
                "ENDS_SENTENCE"
              ],
              "value": ".",
              "display_as": ".",
              "end_time": 6590,
              "type": "punctuation"
            }
          ],
          "start_time": 6130,
          "end_time": 6590,
          "confidence_score": 0.975
        }
      ]
    },
    {
      "start_time": 6590,
      "interpolated": true,
      "speaker_change": false,
      "end_time": 13079,
      "sequences": [
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 6590,
              "tags": [],
              "value": "we",
              "display_as": "We",
              "end_time": 6880,
              "type": "word"
            }
          ],
          "start_time": 6590,
          "end_time": 6880,
          "confidence_score": 0.945
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 6880,
              "tags": [],
              "value": "talked",
              "display_as": "talked",
              "end_time": 7080,
              "type": "word"
            }
          ],
          "start_time": 6880,
          "end_time": 7080,
          "confidence_score": 0.172
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 7080,
              "tags": [],
              "value": "a",
              "display_as": "a",
              "end_time": 7120,
              "type": "word"
            }
          ],
          "start_time": 7080,
          "end_time": 7120,
          "confidence_score": 0.776
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 7120,
              "tags": [],
              "value": "little",
              "display_as": "little",
              "end_time": 7530,
              "type": "word"
            }
          ],
          "start_time": 7120,
          "end_time": 7530,
          "confidence_score": 0.966
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 7530,
              "tags": [],
              "value": "bit",
              "display_as": "bit",
              "end_time": 7960,
              "type": "word"
            }
          ],
          "start_time": 7530,
          "end_time": 7960,
          "confidence_score": 0.973
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 7960,
              "tags": [],
              "value": "in",
              "display_as": "in",
              "end_time": 8060,
              "type": "word"
            }
          ],
          "start_time": 7960,
          "end_time": 8060,
          "confidence_score": 0.868
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 8060,
              "tags": [],
              "value": "the",
              "display_as": "the",
              "end_time": 8600,
              "type": "word"
            }
          ],
          "start_time": 8060,
          "end_time": 8600,
          "confidence_score": 0.968
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 8600,
              "tags": [],
              "value": "past",
              "display_as": "past",
              "end_time": 9009,
              "type": "word"
            }
          ],
          "start_time": 8600,
          "end_time": 9009,
          "confidence_score": 0.967
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 9010,
              "tags": [],
              "value": "video",
              "display_as": "video",
              "end_time": 9270,
              "type": "word"
            }
          ],
          "start_time": 9010,
          "end_time": 9270,
          "confidence_score": 0.977
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 9270,
              "tags": [],
              "value": "about",
              "display_as": "about",
              "end_time": 10540,
              "type": "word"
            }
          ],
          "start_time": 9270,
          "end_time": 10540,
          "confidence_score": 0.989
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 10540,
              "tags": [],
              "value": "what",
              "display_as": "what",
              "end_time": 10650,
              "type": "word"
            }
          ],
          "start_time": 10540,
          "end_time": 10650,
          "confidence_score": 0.6
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 10650,
              "tags": [],
              "value": "is",
              "display_as": "is",
              "end_time": 11170,
              "type": "word"
            }
          ],
          "start_time": 10650,
          "end_time": 11170,
          "confidence_score": 0.972
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 11170,
              "tags": [],
              "value": "real",
              "display_as": "real",
              "end_time": 11350,
              "type": "word"
            }
          ],
          "start_time": 11170,
          "end_time": 11350,
          "confidence_score": 0.902
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 11350,
              "tags": [],
              "value": "time",
              "display_as": "time",
              "end_time": 11719,
              "type": "word"
            }
          ],
          "start_time": 11350,
          "end_time": 11719,
          "confidence_score": 0.957
        },
        {
          "tokens": [
            {
              "interpolated": false,
              "start_time": 11719,
              "tags": [],
              "value": "event",
              "display_as": "event",
              "end_time": 12430,
              "type": "word"
            },
            {
              "interpolated": false,
              "start_time": 12430,
              "tags": [
                "ENDS_SENTENCE"
              ],
              "value": ".",
              "display_as": ".",
              "end_time": 13079,
              "type": "punctuation"
            }
          ],
          "start_time": 11719,
          "end_time": 13079,
          "confidence_score": 0.888
        }
      ]
    }
  ]
}"""

class ElConverterTests(unittest.TestCase):

  def test(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_no_speakers(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_exclude_tags(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()