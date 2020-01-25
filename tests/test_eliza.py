import unittest
from src.utils.eliza import Eliza
from src.constants.constants import KINGDOMS, UNIVERSE

class testMessage(unittest.TestCase):       

    def test_message_for_land(self):
        Eliza._potential_king='Shan'
        recipient_kingdom = 'land'
        messages = ['hello all mighthy','pand','we a have a pen in the drawer',\
                    'pen paper scissor stone d','pen paper stone dart']
        expected_result = [0,0,1,0,1]
        for index,message in enumerate(messages):
            result = Eliza.is_msg_authentic(recipient_kingdom = \
                        recipient_kingdom,message = message,kingdoms=\
                            KINGDOMS)
            if expected_result[index]:
                self.assertTrue(result)
            else:
                self.assertFalse(result)

    
    def test_message_for_air(self):
        Eliza._potential_king='Shan'
        recipient_kingdom = 'air'
        messages = ['hello all mighthy','our well known','can we do ill',\
                    'pen paper scissor stone d','pen paper stone dart']
        expected_result = [0,1,1,0,0]
        for index,message in enumerate(messages):
            result = Eliza.is_msg_authentic(recipient_kingdom = \
                        recipient_kingdom,message = message,kingdoms=\
                            KINGDOMS)
            if expected_result[index]:
                self.assertTrue(result)
            else:
                self.assertFalse(result)

    def test_message_for_fire(self):
        Eliza._potential_king='Shan'
        recipient_kingdom = 'fire'
        messages = ['dont lose the race g','our well known','drag on',\
                    'they think well','gone in the drawer']
        expected_result = [1,0,1,0,1]
        for index,message in enumerate(messages):
            result = Eliza.is_msg_authentic(recipient_kingdom = \
                        recipient_kingdom,message = message,kingdoms=\
                            KINGDOMS)
            if expected_result[index]:
                self.assertTrue(result)
            else:
                self.assertFalse(result)

    def test_message_for_ice(self):
        Eliza._potential_king='Shan'
        recipient_kingdom = 'ice'
        messages = ['dont lose the race g','our well known','mummyat h port',\
                    'hmmm ,said porter','moth is mam Lepidoptera']
        expected_result = [0,0,1,1,1]
        for index,message in enumerate(messages):
            result = Eliza.is_msg_authentic(recipient_kingdom = \
                        recipient_kingdom,message = message,kingdoms=\
                            KINGDOMS)
            if expected_result[index]:
                self.assertTrue(result)
            else:
                self.assertFalse(result)

    def test_message_for_water(self):
        Eliza._potential_king='Shan'
        recipient_kingdom = 'water'
        messages = ['octogon with pipe us','we all won','all is well',\
                    'paint the us flag in october','p and s in the u to orc']
        expected_result = [1,0,0,1,1]
        for index,message in enumerate(messages):
            result = Eliza.is_msg_authentic(recipient_kingdom = \
                        recipient_kingdom,message = message,kingdoms=\
                            KINGDOMS)
            if expected_result[index]:
                self.assertTrue(result)
            else:
                self.assertFalse(result)

    def test_message_for_space(self):
        Eliza._potential_king='Po'
        recipient_kingdom = 'space'
        messages = ['go in the rail lol','sangarila land gone air',\
                    'let us celebrate','Boar is not goar','dead end']
        expected_result = [1,1,0,0,0]
        for index,message in enumerate(messages):
            result = Eliza.is_msg_authentic(recipient_kingdom = \
                        recipient_kingdom,message = message,kingdoms=\
                            KINGDOMS)
            if expected_result[index]:
                self.assertTrue(result)
            else:
                self.assertFalse(result)
        
if __name__ == '__main__':
    unittest.main()