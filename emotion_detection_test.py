import unittest
from EmotionDetection.emotion_detection import emotion_detector  

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        statement = "I am glad this happened"
        expected = "joy"
        result = emotion_detector(statement)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_anger(self):
        statement = "I am really mad about this"
        expected = "anger"
        result = emotion_detector(statement)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_disgust(self):
        statement = "I feel disgusted just hearing about this"
        expected = "disgust"
        result = emotion_detector(statement)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_sadness(self):
        statement = "I am so sad about this"
        expected = "sadness"
        result = emotion_detector(statement)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_fear(self):
        statement = "I am really afraid that this will happen"
        expected = "fear"
        result = emotion_detector(statement)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
