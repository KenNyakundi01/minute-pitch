import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
   
    def setUp(self):
       
        self.new_pitch = Pitch(12, "Test Pitch", "Pitch Description", "Pitch Category")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))