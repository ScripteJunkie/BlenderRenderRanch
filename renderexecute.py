#import Blender
import os
import glob
import sessionkeygenerator as sk

folder = "C:/BlenderRenderRanch/RenderBarn/"

def render():
    files_path = os.path.join(folder, '*')
    files = sorted(
        glob.iglob(files_path), key=os.path.getctime, reverse=True)
    print(files[0])
    #fname = input("Name of blend file: ")
    fname = files[0]
    sname = sk.sname
    os.rename(r''+fname,r'C:/BlenderRenderRanch/RenderBarn/' + sname + '.blend')
    os.chdir("C:/Program Files/Blender Foundation/Blender 2.82")
    #print(os.getcwd())
    #os.system("blender.exe -b C:/BlenderRenderRanch/RenderBarn/" + fname + ".blend -o C:/BlenderRenderRanch/FinalCuts/ -f 1")
    os.system("blender.exe -b " + folder + sname + ".blend" + " -o C:/BlenderRenderRanch/FinalCuts/ -f 1")
