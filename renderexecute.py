#import Blender
import os
import glob
import sessionkeygenerator as sk
import platform

folder = ""

if (platform.system() == "Linux"):
    folder = "/home/machine01/BlenderRenderRanch/RenderBarn/"
else:
    folder = "C:/BlenderRenderRanch/RenderBarn/"

folderout = ""

if (platform.system() == "Linux"):
    folderout = "/home/machine01/BlenderRenderRanch/FinalCuts/"
else:
    folderout = "C:/BlenderRenderRanch/FinalCuts/"

def render():
    files_path = os.path.join(folder, '*')
    files = sorted(
        glob.iglob(files_path), key=os.path.getctime, reverse=True)
    print(files[0])
    #fname = input("Name of blend file: ")
    fname = files[0]
    sname = sk.sname
    os.rename(r''+fname,r''+ folder + sname + '.blend')
    if (platform.system() == 'Linux'):
        os.chdir("/lib/blender-2.82-linux64")
    else:
        os.chdir("C:/Program Files/Blender Foundation/Blender 2.82")
    #print(os.getcwd())
    #os.system("blender.exe -b C:/BlenderRenderRanch/RenderBarn/" + fname + ".blend -o C:/BlenderRenderRanch/FinalCuts/ -f 1")
    if (platform.system() == "Linux"):
        os.system("./blender -b " + folder + sname + ".blend" + " -o " + folderout + " -f 1")
    else:
        os.system("blender.exe -b " + folder + sname + ".blend" + " -o " + folderout + " -f 1")
