import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector('I am glad this happened')
        self.assertIn('joy', result)

unittest.main()