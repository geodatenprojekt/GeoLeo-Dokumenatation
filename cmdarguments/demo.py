import cmdargs

cmdargs = cmdargs.Parameters()


print("output path:",cmdargs.getOutputPath())
print("cadaster path:",cmdargs.getCadasterPath())
print("pointcloud path:",cmdargs.getPointCloudPath())
print("x-offset:",cmdargs.getXOffset())
print("y-offset:",cmdargs.getYOffset())