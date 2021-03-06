#!/usr/bin/python

import json
import yaml
import os.path
from mdutils import MdUtils

base_url = "https://github.com/openrba/python-azure-techradar/tree/master"

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
                'url': path + resourceType,
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
            
            processPath(current_path+key+'/',key,(index+1),'HOLD')

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
    
    adopt_tbl = [
        "<sub>Resource</sub>",
        "<sub>Description</sub>",
        "<sub>Type</sub>",
        "<sub>Status</sub>"
    ]
    adopt_cnt = len(adopt_list) + 1
   
    for key in adopt_list:
        resourceName    = key
        resourceDesc    = data[key].get("description","")
        resourcePath    = data[key].get("path","")
        resourceType    = data[key].get("architecture review","").get("type","")
        resourceUrl     = data[key].get("url","")
        resourceStatus    = data[key].get("status","")
        resourceName    = "["+resourceName+"]("+base_url+'/'+resourceUrl+")"
        adopt_tbl.extend([
            '<sub>' + resourceName + '</sub>',
            '<sub>' + resourceDesc + '</sub>',
            '<sub>' + resourceType + '</sub>',
            '<sub>' + resourceStatus + '</sub>'
        ])
    
    if adopt_cnt == 1:
        mdf.new_line("")
        mdf.new_line("There are currently no resources at this ring level.",bold_italics_code='bi', color='red')
    else:
        mdf.new_line("")
        mdf.new_table(columns=4,rows=adopt_cnt,text=adopt_tbl)

    # Handle the Trial Section
    mdf.new_header(level=3, title='Trial')
    mdf.new_paragraph("Technologies that we have seen work with success in projects "
    "to solve real problems;  first serious usage experience that confirm benefits "
    "and uncover limitations.  TRIAL technologies are slightly more risky; some "
    "engineers in our organization walked this path and will share knowledge and "
    "experiences.  This area can contain services that have been architecture and "
    "security reviewed but do not contain automated policy managmeent."
    )

    trial_tbl = [
        "<sub>Resource</sub>",
        "<sub>Description</sub>",
        "<sub>Type</sub>",
        "<sub>Status</sub>"
    ]
    trial_cnt = len(trial_list) + 1
    for key in trial_list:
        resourceName    = key
        resourceDesc    = data[key].get("description","")
        resourcePath    = data[key].get("path","")
        resourceType    = data[key].get("architecture review","").get("type","")
        resourceUrl     = data[key].get("url","")
        resourceStatus    = data[key].get("status","")
        resourceName    = "["+resourceName+"]("+base_url+'/'+resourceUrl+")"
        trial_tbl.extend([
            '<sub>' + resourceName + '</sub>',
            '<sub>' + resourceDesc + '</sub>',
            '<sub>' + resourceType + '</sub>',
            '<sub>' + resourceStatus + '</sub>'
        ])
    
    if trial_cnt == 1:
        mdf.new_line("")
        mdf.new_line("There are currently no resources at this ring level.",bold_italics_code='bi', color='red')
    else:
        mdf.new_line("")
        mdf.new_table(columns=4,rows=trial_cnt,text=trial_tbl) 

    # Handle the Assess Section
    mdf.new_header(level=3, title='Assess')
    mdf.new_paragraph("Technologies that are promising and have clear potential "
    "value-add for us; technologies worth investing some research and "
    "prototyping efforts to see if it has impact.  ASSESS technologies have "
    "higher risks;  they are often new to our organization and highly unproven "
    "within RBA.  You will find some engineers that have knowledge in the "
    "technology and promote it, you may even find teams that have started "
    "a prototyping effort.  These technologies can also include services that "
    "are currently in architecture or security review."
    )

    assess_tbl = [
        "<sub>Resource</sub>",
        "<sub>Description</sub>",
        "<sub>Type</sub>",
        "<sub>Status</sub>"
    ]
    assess_cnt = len(assess_list) + 1
    for key in assess_list:
        resourceName    = key
        resourceDesc    = data[key].get("description","")
        resourcePath    = data[key].get("path","")
        resourceType    = data[key].get("architecture review","").get("type","")
        resourceUrl     = data[key].get("url","")
        resourceStatus    = data[key].get("status","")
        resourceName    = "["+resourceName+"]("+base_url+'/'+resourceUrl+")"
        assess_tbl.extend([
            '<sub>' + resourceName + '</sub>',
            '<sub>' + resourceDesc + '</sub>',
            '<sub>' + resourceType + '</sub>',
            '<sub>' + resourceStatus + '</sub>'
        ])
    
    if assess_cnt == 1:
        mdf.new_line("")
        mdf.new_line("There are currently no resources at this ring level.",bold_italics_code='bi', color='red')
    else:
        mdf.new_line("")
        mdf.new_table(columns=4,rows=assess_cnt,text=assess_tbl) 

    # Handle the Hold Section
    mdf.new_header(level=3, title='Hold')
    mdf.new_paragraph("Technologies not recommended to be used for new projects. "
    "Technologies that we think are not (yet) worth to (further) invest in.  "
    "HOLD technologies should not be used for new projects, but usually can be "
    "continued for existing projects.  These technologies may include services "
    "that have yet to be evaluated by architecture and security due to a lack "
    "of interest, time, or need."
    )

    hold_tbl = [
        "<sub>Resource</sub>",
        "<sub>Description</sub>",
        "<sub>Type</sub>",
        "<sub>Status</sub>"
    ]

    hold_cnt = len(hold_list) + 1
    for key in hold_list:
        resourceName    = key
        resourceDesc    = data[key].get("description","")
        resourcePath    = data[key].get("path","")
        resourceType    = data[key].get("architecture review","").get("type","")
        resourceUrl     = data[key].get("url","")
        resourceStatus    = data[key].get("status","")
        #resourceName    = "["+resourceName+"]("+resourceUrl+")"
        hold_tbl.extend([
            '<sub>' + resourceName + '</sub>',
            '<sub>' + resourceDesc + '</sub>',
            '<sub>' + resourceType + '</sub>',
            '<sub>' + resourceStatus + '</sub>'
        ])
    
    if hold_cnt == 1:
        mdf.new_line("")
        mdf.new_line("There are currently no resources at this ring level.",bold_italics_code='bi', color='red')
    else:
        mdf.new_line("")
        mdf.new_table(columns=4,rows=hold_cnt,text=hold_tbl)    


    # Handle the Reject Section
    mdf.new_header(level=3, title='Reject')
    mdf.new_paragraph("Technologies not recommended to be used for any projects. "
    "Technologies that have undergone architecture and security review but do "
    "not meet company standards for use.  REJECT technologies should never be "
    "used on any project and should be considered deprecated for existing "
    "projects."
    )

    reject_tbl = [
        "<sub>Resource</sub>",
        "<sub>Description</sub>",
        "<sub>Type</sub>",
        "<sub>Status</sub>"
    ]
    reject_cnt = len(reject_list) + 1
    for key in reject_list:
        resourceName    = key
        resourceDesc    = data[key].get("description","")
        resourcePath    = data[key].get("path","")
        resourceType    = data[key].get("architecture review","").get("type","")
        resourceUrl     = data[key].get("url","")
        resourceStatus    = data[key].get("status","")
        #resourceName    = "["+resourceName+"]("+resourceUrl+")"
        reject_tbl.extend([
            '<sub>' + resourceName + '</sub>',
            '<sub>' + resourceDesc + '</sub>',
            '<sub>' + resourceType + '</sub>',
            '<sub>' + resourceStatus + '</sub>'
        ])
    
    if reject_cnt == 1:
        mdf.new_line("")
        mdf.new_line("There are currently no resources at this ring level.",bold_italics_code='bi', color='red')
    else:
        mdf.new_line("")
        mdf.new_table(columns=4,rows=reject_cnt,text=reject_tbl) 

    mdf.create_md_file()

def main():
# Main function
    processPath('','',0,'HOLD')    

if __name__ == '__main__':
    main()