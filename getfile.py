import os
import json

def build_file_tree(directory):
    file_tree = {}
    for root, dirs, files in os.walk(directory):
        path = root.split(os.sep)
        
        found = False
        for item in path:
            if "releases" in item:
                found = True
                break

        if found == False:
            continue

        sub_tree = file_tree
        for folder in path[1:]:
            #print("folder name: ", folder)
            sub_tree = sub_tree.setdefault(folder, {})
        sub_tree.update({file: None for file in files})
    return file_tree

def main():
    directory = os.getcwd()  # 替换为您的目标目录
    file_tree = build_file_tree(directory)
    with open('fileTree.json', 'w', encoding='utf-8') as f:
        json.dump(file_tree, f, ensure_ascii=False, indent=2)
    print('File tree generated successfully.')

if __name__ == "__main__":
    main()
