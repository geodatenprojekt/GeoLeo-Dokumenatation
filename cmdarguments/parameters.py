import argparse
parser = argparse.ArgumentParser(prog='Geodatenverarbeitung')

filehandling = parser.add_argument_group('file handling (ALL OR NONE)')
filehandling.add_argument("--cadaster", "-c", help="path to cadaster directory")
filehandling.add_argument("--pointcloud", "-p", help="path to pointcloud directory")
filehandling.add_argument("--directory", "-d", help="path to output directory")

parser.add_argument("--xoffset", "-x", type=float, default=0, help="float expected, offset in direction x")
parser.add_argument("--yoffset", "-y", type=float, default=0, help="flaot expected, offset in direction y")
parser.add_argument('--version', "-v", action='version', version='%(prog)s 0.1')

args = parser.parse_args()

