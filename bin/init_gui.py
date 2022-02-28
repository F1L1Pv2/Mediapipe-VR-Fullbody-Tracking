import tkinter as tk
import pickle
import cv2

def getparams():
    
    try:
        param = pickle.load(open("params.p","rb"))
    except:
        param = {}
        
    if "camid" not in param:
        param["camid"] = 'http://192.168.1.103:8080/video'
    if "imgsize" not in param:
        param["imgsize"] = 800
    if "neckoffset" not in param:
        param["neckoffset"] = [0.0, -0.2, 0.1]
    if "prevskel" not in param:
        param["prevskel"] = False
    if "waithmd" not in param:
        param["waithmd"] = False
    if "rotateclock" not in param:
        param["rotateclock"] = False
    if "rotatecclock" not in param: 
        param["rotatecclock"] = False
    if "rotate" not in param:
        param["rotate"] = None
    if "camlatency" not in param:
        param["camlatency"] = 0.05
    if "smooth" not in param:
        param["smooth"] = 0.5
    if "feetrot" not in param:
        param["feetrot"] = False
    if "calib_scale" not in param:
        param["calib_scale"] = True
    if "calib_tilt" not in param:
        param["calib_tilt"] = True
    if "calib_rot" not in param:
        param["calib_rot"] = True
    if "use_hands" not in param:
        param["use_hands"] = False
    if "ignore_hip" not in param:
        param["ignore_hip"] = False
    if "camera_settings" not in param:
        param["camera_settings"] = False
    if "camera_width" not in param:
        param["camera_width"] = 640
    if "camera_height" not in param:
        param["camera_height"] = 480

    window = tk.Tk()

    tk.Label(text="Camera IP or ID:", width = 50).pack()
    camid = tk.Entry(width = 50)
    camid.pack()
    camid.insert(0,param["camid"])
    
    tk.Label(text="NOTE: Increasing resolution may decrease performance.\n Unless you have problems with opening camera, leave it at default.", width = 50).pack()

    tk.Label(text="Camera width:", width = 50).pack()
    camwidth = tk.Entry(width = 20)
    camwidth.pack()
    camwidth.insert(0,param["camera_width"])
    
    tk.Label(text="Camera height:", width = 50).pack()
    camheight = tk.Entry(width = 20)
    camheight.pack()
    camheight.insert(0,param["camera_height"])
    
    varcamsettings = tk.IntVar(value = param["camera_settings"])
    cam_settings_check = tk.Checkbutton(text = "Attempt to open camera settings", variable = varcamsettings)
    cam_settings_check.pack()

    tk.Label(text="Maximum image size:", width = 50).pack()
    maximgsize = tk.Entry(width = 20)
    maximgsize.pack()
    maximgsize.insert(0,param["imgsize"])

    tk.Label(text="Offset of HMD to neck:", width = 50).pack()
    hmdoffsettext = tk.Entry(width = 50)
    hmdoffsettext.pack()
    hmdoffsettext.insert(0," ".join(map(str,param["neckoffset"])))
    
    if False:
        tk.Label(text="Smoothing:", width = 50).pack()
        smoothingtext = tk.Entry(width = 50)
        smoothingtext.pack()
        smoothingtext.insert(0,param["smooth"])
        
        tk.Label(text="Camera latency:", width = 50).pack()
        camlatencytext = tk.Entry(width = 50)
        camlatencytext.pack()
        camlatencytext.insert(0,param["camlatency"])

    """
    varhmdwait = tk.IntVar(value = param["waithmd"])
    hmdwait_check = tk.Checkbutton(text = "Dont wait for hmd", variable = varhmdwait)
    hmdwait_check.pack()
    """
    if False:
        varclock = tk.IntVar(value = param["rotateclock"])
        rot_clock_check = tk.Checkbutton(text = "Rotate camera clockwise", variable = varclock)
        rot_clock_check.pack()

        varcclock = tk.IntVar(value = param["rotatecclock"])
        rot_cclock_check = tk.Checkbutton(text = "Rotate camera counter clockwise", variable = varcclock)
        rot_cclock_check.pack()
    
    varfeet = tk.IntVar(value = param["feetrot"])
    rot_feet_check = tk.Checkbutton(text = "Enable experimental foot rotation", variable = varfeet)
    rot_feet_check.pack()

    if False:
    
        varscale = tk.IntVar(value = param["calib_scale"])
        scale_check = tk.Checkbutton(text = "Enable automatic scale calibration", variable = varscale)
        scale_check.pack()
        
        vartilt = tk.IntVar(value = param["calib_tilt"])
        tilt_check = tk.Checkbutton(text = "Enable automatic tilt calibration", variable = vartilt)
        tilt_check.pack()
    
        varrot = tk.IntVar(value = param["calib_rot"])
        rot_check = tk.Checkbutton(text = "Enable automatic rotation calibration", variable = varrot)
        rot_check.pack()
    
    varhip = tk.IntVar(value = param["ignore_hip"])
    hip_check = tk.Checkbutton(text = "Don't use hip tracker", variable = varhip)
    hip_check.pack()
    
    tk.Label(text="-"*50, width = 50).pack()
    
    varhand = tk.IntVar(value = param["use_hands"])
    hand_check = tk.Checkbutton(text = "DEV: spawn trackers for hands", variable = varhand)
    hand_check.pack()
    
    varskel = tk.IntVar(value = param["prevskel"])
    skeleton_check = tk.Checkbutton(text = "DEV: preview skeleton in VR", variable = varskel)
    skeleton_check.pack()

    tk.Button(text='Save and continue', command=window.quit).pack()

    window.mainloop()

    cameraid = camid.get()
    maximgsize = int(maximgsize.get())
    hmd_to_neck_offset = [float(val) for val in hmdoffsettext.get().split(" ")]
    preview_skeleton = bool(varskel.get())
    dont_wait_hmd = False #bool(varhmdwait.get()) 
    
    #camera_latency = float(camlatencytext.get())
    #smoothing = float(smoothingtext.get())
    feet_rotation = bool(varfeet.get())
    use_hands = bool(varhand.get())
    ignore_hip = bool(varhip.get())
    camera_settings = bool(varcamsettings.get())
    camera_height = camheight.get()
    camera_width = camwidth.get()

    param = {}
    param["camid"] = cameraid
    param["imgsize"] = maximgsize
    param["neckoffset"] = hmd_to_neck_offset
    param["prevskel"] = preview_skeleton
    param["waithmd"] = dont_wait_hmd

    #param["smooth"] = smoothing
    #param["camlatency"] = camera_latency
    param["feetrot"] = feet_rotation
    param["use_hands"] = use_hands
    param["ignore_hip"] = ignore_hip
    
    param["camera_settings"] = camera_settings
    param["camera_height"] = camera_height
    param["camera_width"] = camera_width
    
    pickle.dump(param,open("params.p","wb"))
    
    window.destroy()
    
    return param

if __name__ == "__main__":
    print(getparams())