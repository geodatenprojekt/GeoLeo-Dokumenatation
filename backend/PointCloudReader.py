from laspy.file import File
import numpy as np
import util


"""
Class PointCloudFileIO encapsulates read/write access to .laz/.las files
The PointClouds can be read from either format, however .laz files will be
unzipped to .las files beforehands
"""
class PointCloudFileIO:

    """
    Constructs PointCloudFileIO object and reads PointCloud file by default

    @param path  The path to the .las/.laz file
    @param read  Whether or not the file should be read immediately
    """
    def __init__(self, path, read=True):
        self.path = path
        self.file = None

        if(read):
            self.readFile()

    def __del__(self):
        if(self.file != None):
            self.file.close()


    """
    Reads and parses the files content
    If the file is a .laz file, it will be automatically unzipped to a .las file
    """
    def readFile(self):
        if(self.path.endswith(".laz")): #Further unpacking from LAZ to LAS needed
            util.unzipLAZFile(self.path)
            self.path = ".laz".join(self.path.split(".laz")[0:-1]) + ".las"

        self.file = File(self.path, mode='r')


    """
    Saves the input file to a specified output file.
    Can save only certain points in the PointCloud if needed.

    @param path  The path to the new file
    @param keepPoints  An array of booleans to determine which points are saved. Needs to have the same length as the points array
    """
    def writeFileToPath(self, path, keepPoints=None):
        if(self.file != None):
            outFile = File(path, mode='w', header=self.file.header)
            if(keepPoints == None):
                outFile.points = self.file.points
            else:
                outFile.points = self.file.points[keepPoints]
            outFile.close()


    """
    Returns all points in the PointCloud, see below for a thorough example
    """
    def getPoints(self):
        return self.file.points

    def getPath(self):
        return self.path

    def getFile(self):
        return self.file




"""
=== Explanation of the points array ===


# PointCloudFileIO.getPoints() returns a numpy array of points in this form:
# point = tuple(tuple(i4, i4, i4, u2, u1, u1, i1, u1, u2, u2, u2, u2),)

# This means a point in this array looks like this with semantics:
# point = ((x, y, z, intensity, flag_byte, raw_classification, scan_angle_rank, user_data, pt_src_id, red, green, blue),)

# And like this with example values:
# point = ((11683, 25476,   8710, 0, 32, 0, 0, 0, 364, 19380, 21165, 23205),)

# All numpy functions can be used to create a modified version of the points array


=== Example usage of class PointCloudReader ===


# Create new PointCloudFileIO object with the path to the laz/las file as parameter
pcReader = PointCloudFileIO(util.getPathToFile("example_data/47078_575419_0011.laz"))

points = pcReader.getPoints()
print(points[0]) # The first point in the list
print(points[0][0][0]) # The x coordinate of the first point
print(points[0][0][1]) # The y coordinate of the first point
print(points[0][0][2]) # The z coordinate of the first point

pcReader.writeFileToPath(util.getPathToFile("test.las")) # Write the input file to another file


# More examples of modifying the points array:
# https://pythonhosted.org/laspy/tut_part_1.html
"""
