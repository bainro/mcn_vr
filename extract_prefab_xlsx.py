import os
import csv

resources_dir = r"/home/rbain/git/mcn_vr/Unity3D/Assets/Resources/3D/ResourcesWindows/"
resource_files = os.listdir(resources_dir)
with open('Prefab ID Sheet.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "ID"]
    writer.writerow(field)
    for f in resource_files:
        if f.endswith(".meta"):
            fullpath = os.path.join(resources_dir, f)
            with open(fullpath, 'r') as meta_f:
                lines = meta_f.readlines()    
                for l in lines:
                    if len(l) > len('guid: '):
                        if l[:6] == 'guid: ':
                            guid = l[6:]          
                            # remove the '.meta'
                            writer.writerow([f[:-5], guid])