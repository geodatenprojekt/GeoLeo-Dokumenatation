import unittest
from backend import PointCloudReader

class Test_PointCloudReader(unittest.TestCase):
    def setUp(self):
        pass


    """
    If the PointCloudFileIO object do not  get a valid path 
    of a .las/.laz file it should throws an OSError
    """
    def test_readFile_NoFile(self):
        with self.assertRaises(OSError):
            PointCloudReader.PointCloudFileIO("No File")



    def tearDown(self) -> None:
        pass