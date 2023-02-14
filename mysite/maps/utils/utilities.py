def dictform_to_list(dict):
    value = dict['fileNames'].split(",")
    files = value[:-1:]
    return files
