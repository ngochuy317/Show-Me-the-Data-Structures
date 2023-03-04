import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    list_of_paths = []
    if suffix == '':
        return list_of_paths
    
    list_dir = os.listdir(path)
    
    if len(list_dir) == 0:
        return list_of_paths
    
    folders = []
    for ele in list_dir:
        if f".{suffix}" in ele:
            list_of_paths.append(os.path.join(path, ele))
        elif "." not in ele:
            folders.append(ele)


    for folder in folders:
        list_of_paths.extend(find_files(suffix, os.path.join(path, folder)))

    return list_of_paths

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
path_base = os.getcwd() + '/testdir'
# Test Case 1
print(find_files(suffix='c', path=path_base))

# Test Case 2
print(find_files(suffix='', path=path_base))

# Test Case 3
print(find_files(suffix='x', path=path_base))
