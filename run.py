#!/usr/bin/python

import json
import yaml
import os.path
from mdutils import MdUtils

base_url = "https://github.com/openrba/python-azure-techradar"

def createResourceDict(data,value,index,default,path):
# Creates a dictionary of resourceTypes

    output = dict()

    #pre = '/' if index > 0 else ''

    for element in data:
        resource_list = element.split("/")

        if len(resource_list) > index:
            resourceType = resource_list[index]
        else:
            continue

        if resourceType not in output.keys():

            output[resourceType] = {
                
                'path': path + resourceType,
                'description': 'UNKNOWN',
                'status': default,
                'url': path + resourceType + '/README.md',
                'architecture review' : {
                    'type': 'UNKNOWN',
                    'status': 'NOT REVIEWED',
                    'start' : 'NOT STARTED',
                    'end' : 'NOT ENDED',
                    'notes' : 'There are no architectural notes for this service at this time.'
                },
                'security review' : {
                    'class': 'UNKNOWN',
                    'status': 'NOT REVIEWED',
                    'start' : 'NOT STARTED',
                    'end' : 'NOT ENDED',
                    'notes': 'There are no security notes for this service at this time.'
                }
            }
    
   
    return output

def openCustomYaml(path):
# Opens yaml config file at <path> and returns
# data in dictionary
    if os.path.isfile(path): 
        
        data = yaml.load(
                        open(path),
                        Loader=yaml.FullLoader
                        )
        return data
    else:
        return False

def openJson(path):
# Opens json file at <path> and returns data in 
# dictionary
    
    with open(path) as json_file:
        data = json.load(json_file)
    
    return data

def findChildren(current_dict,current_data,current_path,search,index):
# Find the subdirectories under this one

    for key in current_dict:
        if (current_dict[key].get("status") in ("ADOPT", "TRIAL", "ASSESS")):
        
            current_status = current_dict[key].get("status")
            
            resource_list = list()

            for element in current_data:
                if index == 0: current_path = ''
                if (current_path + key+'/') in element: resource_list.append(element)
            
            if len(resource_list) == 0: continue

            if not os.path.isdir(current_path + key):
                os.makedirs(current_path + key)

            if not os.path.isfile(current_path + key + '/resource.json'):

                with open(current_path + key + '/resource.json', 'w+') as f:
                    json.dump(resource_list, f, indent=4)
            
            processPath(current_path+key+'/',key,(index+1),current_status)

def processPath(path,search,index,default):
# Gets the resources and the custom and combines them together
# to form the new README
    
    data = openJson(path + 'resource.json')
    resource_dict = createResourceDict(data ,search, index,default,path)
    
    if openCustomYaml(path + 'main.yml'):
        main_dict = openCustomYaml(path + 'main.yml')
    else:
        main_dict = {}
    
    combined_dict = {**resource_dict, **main_dict}
    
    f = open(path + 'main.yml','w+')
    yaml.dump(combined_dict, f, default_flow_style=False, sort_keys=False)

    makeMarkdown(combined_dict,path)
    findChildren(combined_dict, data, path, search, index)  

def makeMarkdown(data,path):
# Creates the README file
    global base_url

    mdf = MdUtils(file_name=path+'README',title='RBA TechRadar for Azure')
    
    adopt_list  = list()
    trial_list  = list()
    assess_list = list()
    hold_list   = list()
    reject_list = list()
    
    # Create categories on status
    for key in data:
        status = data[key].get("status")
        if status == "ADOPT": adopt_list.append(key)
        if status == "TRIAL": trial_list.append(key)
        if status == "ASSESS": assess_list.append(key)
        if status == "HOLD": hold_list.append(key)
        if status == "REJECT": reject_list.append(key)
    
    mdf.new_header(level=1, title='Overview')
    
    mdf.new_header(level=2, title='What is the purpose?')
    mdf.new_paragraph("The RBA TechRadar for Azure is a tool to inspire and "
    "support engineering teams at Risk & Business Analytics to pick the best "
    "technologies for new projects; it provides a platform to share knowledge "
    "and experience in technologies, to reflect on technology decisions and "
    "continuously evolve our technology landscape.  Based on the pioneering "
    "work at Thought Works, our radar sets out the changes in technologies "
    "that are interesting in cloud development - changes that we think our "
    "engineering teams should pay attention to and consider using in their "
    "projects."
    )

    mdf.new_header(level=2, title='How do we maintain it?')
    mdf.new_paragraph("The RBA TechRadar for Azure is maintained by the Cloud "
    "Center of Excellence - an open group of senior RBA technologists committed "
    "to devote time to this purpose.  The CCoE self organizes to maintain these "
    "documents, including this version.  Assignment of technologies to rings is "
    "the outcome of status change proposals, which are discussed and voted on "
    "in CCoE meetings.  The radar depends on active participation and input from "
    "all engineering teams at RBA."
    )
    
    mdf.new_header(level=2, title='What are the current ring assignments?')
    mdf.new_paragraph("The RBA TechRadar for Azure is a list of technologies, "
    "complemented by an assesment result, called ring assignment.  We use five "
    "rings with the following semantics:"
    )

    # Handle the Adopt Section
    mdf.new_header(level=3, title='Adopt')
    mdf.new_paragraph("Technologies we have high confidence in to serve our "
    "purpose, also at large scale.  Technologies with a usage culture in the "
    "RBA production environment, low risk, automated policy enforcement and "
    "are recommended to be widely used."
    )
    
    adopt_tbl = ["Resource","Description","Path","Status"]
    adopt_cnt = len(adopt_list) + 1
   
    for key in adopt_list:
        resourceName    = key
        resourceDesc    = data[key].get("description","")
        resourcePath    = data[key].get("path","")
        resourceUrl     = data[key].get("url","")
        resourceStatus    = data[key].get("status","")
        resourceName    = "["+resourceName+"]("+base_url+'/'+resourceUrl+")"
        adopt_tbl.extend([resourceName,resourceDesc,resourcePath,resourceStatus])
    
    if adopt_cnt == 1:
        mdf.new_line("")
        mdf.new_line("There are currently no resources at this ring level.",bold_italics_code='bi', color='red')
    else:
        mdf.new_line("")
        mdf.new_table(columns=4,rows=adopt_cnt,text=adopt_tbl,text_align='center')

    # Handle the Hold Section
    mdf.new_header(level=3, title='Hold')
    mdf.new_paragraph("Technologies not recommended to be used for new projects. "
    "Technologies that we think are not (yet) worth to (further) invest in.  "
    "HOLD technologies should not be used for new projects, but usually can be "
    "continued for existing projects.  These technologies may include services "
    "that have yet to be evaluated by architecture and security due to a lack "
    "of interest, time, or need."
    )

    hold_tbl = ["Resource","Description","Path","Status"]
    hold_cnt = len(hold_list) + 1
    for key in hold_list:
        resourceName    = key
        resourceDesc    = data[key].get("description","")
        resourcePath    = data[key].get("path","")
        resourceUrl     = data[key].get("url","")
        resourceStatus    = data[key].get("status","")
        #resourceName    = "["+resourceName+"]("+resourceUrl+")"
        hold_tbl.extend([resourceName,resourceDesc,resourcePath,resourceStatus])
    
    if hold_cnt == 1:
        mdf.new_line("")
        mdf.new_line("There are currently no resources at this ring level.",bold_italics_code='bi', color='red')
    else:
        mdf.new_line("")
        mdf.new_table(columns=4,rows=hold_cnt,text=hold_tbl,text_align='center')    

    mdf.create_md_file()

def main():
# Main function
    processPath('','',0,'HOLD')    

if __name__ == '__main__':
    main()