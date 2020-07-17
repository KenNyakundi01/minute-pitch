import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_pitch = Pitch(12, "Test Pitch", "Pitch Description", "Pitch Category")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))