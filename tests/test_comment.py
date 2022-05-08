
import unittest
from app.models import Comments
 
class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Comment class
    '''
        
    def setUp(self):
        self.new_comment= Comments(id=1,pitch_id=2,posted='2022, 3, 7, 7, 19, 10, 319212',comment='This pitch is the best thing since sliced bread',user_id=12 )
        
    def tearDown(self):
        Comments.query.delete()
        
    def test_init(self):
        self.assertEquals(self.new_comment.comment,'This pitch is the best thing since sliced bread')
        self.assertEquals(self.new_comment.user_id,12)
        self.assertEquals(self.new_comment.pitch_id,2)
        self.assertEquals(self.new_comment.posted,'2022, 3, 7, 7, 19, 10, 319212')
        self.assertEquals(self.new_comment.id,1)



    def test_save(self):
        self.new_comment.save()
        self.assertTrue(len(Comments.query.all())>0)
    def test_get_comment(self):

        self.new_comment.save()
        got_comment = Comments.get_comment('Comment for pitches')
        self.assertTrue(len(got_comment) == 1)