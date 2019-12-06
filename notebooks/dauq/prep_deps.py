# todo: deal with linux bins!

import os
import platform
import shutil

py_dirs = [os.path.join("/","Users","jwhite","Dev","pyemu","pyemu"),
           os.path.join("/","Users","jwhite","Dev","flopy","flopy")]

pestpp_bin_dir = os.path.join("/","Users","jwhite","Dev","pestpp","bin")

#mfnwt_bin_dir = os.path.join("/","Users","jeremyw","Dev","pestpp","benchmarks","test_bin")
#mfnwt_bin_dir = os.path.join("..","..","bin")


if "linux" in platform.platform().lower():
    os_d = "linux"
elif "darwin" in platform.platform().lower():
    os_d = "mac"
else:
    os_d = "iwin"

def prep_for_deploy():
    for py_dir in py_dirs:
        dest_dir = os.path.split(py_dir)[-1]
        assert os.path.exists(py_dir),py_dir
        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir)
        shutil.copytree(py_dir,dest_dir)
    
    
   
    for oos_dir in ["linux","mac","iwin"]:
        src_dir = os.path.join(pestpp_bin_dir,oos_dir)
        dest_dir = os.path.join("bin",oos_dir.replace("iwin","win"))

        print(src_dir)
        for src_f in os.listdir(src_dir):
            dest_f = src_f
            if src_f.startswith("i"):
                dest_f = src_f[1:]
            if os.path.exists(os.path.join(dest_dir,dest_f)):
                os.remove(os.path.join(dest_dir,dest_f))

            shutil.copy2(os.path.join(src_dir,src_f),os.path.join(dest_dir,dest_f))


def prep_template(t_d="template"):
    for d in ["pyemu","flopy"]:
        if os.path.exists(os.path.join(t_d,d)):
            shutil.rmtree(os.path.join(t_d,d))
        shutil.copytree(d,os.path.join(t_d,d))
    files = os.listdir(os.path.join("bin",os_d))
    for f in files:
        if os.path.exists(os.path.join(t_d,f)):
            os.remove(os.path.join(t_d,f))
        shutil.copy2(os.path.join("bin",os_d,f),os.path.join(t_d,f))
    
if __name__ == "__main__":
    prep_for_deploy()  
    #prep_template(t_d="temp")  
