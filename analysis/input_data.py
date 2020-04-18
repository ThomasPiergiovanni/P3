import os
import logging as lg
lg.basicConfig(level=lg.DEBUG)

def get_source(data_file):

    # this will render an error if data_file is empty.
    path_to_file = os.path.join("data", data_file)

    file_name = os.path.basename(path_to_file)
    directory = os.path.dirname(path_to_file)
    lg.info("Opening data file {} from directory '{}'".format(file_name,directory))

    try:
        with open(path_to_file,"r") as source_file:
            content = source_file.read()
            lg.debug("Read file Ok. Here is the content:{%s}" % content)
            return content

    except FileNotFoundError as e:
        lg.critical("Ow :( The file was not found. Here is the original message of the exception : {%s}" % e)
    except:
        lg.critical('Destination unknown')


def prepare_data(content):
    element_list=[]
    for elt in content:
        try:
            elt =str(elt)
            if elt == "0":
                element_list.append("wall")
            elif elt == "1":
                element_list.append("path")
            elif elt == "2":
                element_list.append("start")
            elif elt == "3":
                element_list.append("end")
            else:
                pass
        except:
            lg.critical ("Str conversion not done")
    return element_list

def main(data_file):
    content= get_source(data_file)
    content_ready = prepare_data(content)
    return content_ready  

if __name__ == "__main__":
    print("Executed here")
    main(data_file)
else: 
    print("Imported")