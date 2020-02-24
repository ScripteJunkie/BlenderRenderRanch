#import Blender
import os
import glob

folder = "C:\BlenderRenderRanch\RenderBarn"
files_path = os.path.join(folder, '*')
files = sorted(
    glob.iglob(files_path), key=os.path.getctime, reverse=True)
print(files[0])
#fname = input("Name of blend file: ")
fname = files[0]
os.chdir("C:/Program Files/Blender Foundation/Blender 2.82")
#print(os.getcwd())
#os.system("blender.exe -b C:/BlenderRenderRanch/RenderBarn/" + fname + ".blend -o C:/BlenderRenderRanch/FinalCuts/ -f 1")
os.system("blender.exe -b " + fname + " -o C:/BlenderRenderRanch/FinalCuts/ -f 1")
