from static import prompt



files = "file format"


def llm_function(file_input):
    
    # deploys an llm model to summarise text

    return "temp string holder"
    
    
    
    
def file_type(file_input):
    # get file type
    return "temp holder"
    
def parse_text(file_format):
    return "string"

def main():
    # get file format
    file_format = file_type(files)
    
    # parse text
    file_input = parse_text(file_format)
    
    
    # call function to then deploy LLM to summarise text
    summary = llm_function(file_input)
    
    
    