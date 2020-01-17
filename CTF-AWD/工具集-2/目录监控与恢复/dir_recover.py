# coding=gbk
# !/var/bin/python
#coding=utf-8

import sys,os,re,time
import filecmp
import shutil

only_file_path_list = []
diff_file_path_list = []
def dir_comparison(dir1, dir2):
    dircom = filecmp.dircmp(dir1,dir2)
    only_in_one = dircom.left_only
    diff_in_one = dircom.diff_files
    # for file in diff_in_one:
    #     print(time.strftime("%H:%M:%S", time.localtime()) + ":"+ file + "  ")
    source_path = os.path.abspath(dir1)
    backup_path = os.path.abspath(dir2)
    # [backup_list.append(os.path.abspath(os.path.join(dir1, x))) for x in only_in_one]
    [only_file_path_list.append(os.path.join(source_path, item)) for item in only_in_one]
    [diff_file_path_list.append(os.path.join(source_path, item)) for item in diff_in_one]

    if len(dircom.common_dirs) > 0:
        for item in dircom.common_dirs:
            dir_comparison(os.path.abspath(os.path.join(source_path, item)), os.path.abspath(os.path.join(backup_path,item)))

    return only_file_path_list, diff_file_path_list

def only_remove(only_file_path_list):
    if len(only_file_path_list)>0:
        for item in only_file_path_list:
            if os.path.isdir(item):
                try:
                    os.removedirs(item)
                    print(time.strftime("%H:%M:%S", time.localtime()) + " for one scan, found new dir:" + item + ", delete done!")
                except:
                    pass
            else:
                try:
                    os.remove(item)
                    print(time.strftime("%H:%M:%S", time.localtime()) + " for one scan, found new file:" + item + ", delete done!")
                except:
                    pass
    else:
        print(time.strftime("%H:%M:%S", time.localtime()) + " for one scan, no new file!")


def diff_replace(diff_file_path_list, backup_file_path_list):
    copy_file = zip(backup_file_path_list, diff_file_path_list)
    for item in copy_file:
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0], item[1])
    if len(diff_file_path_list) > 0:
        print(time.strftime("%H:%M:%S", time.localtime()) + " found file is change, auto done a new restore, recover file is:")
        for item in diff_file_path_list:
            print(item)
    else:
        print(time.strftime("%H:%M:%S", time.localtime()) + " done a restore, no new file change!restore file 0!")


def main():

    if len(sys.argv) > 2:
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
    else:
        print("python *.py source_dir restore_dir")
        sys.exit()

    # dir1 = "./filecmp/www1"
    # dir2 = "./filecmp/www2"

    only_file_path_list, diff_file_path_list = dir_comparison(dir1, dir2)
    if len(only_file_path_list)>=0:
        print("###start dir scan###")
        only_remove(only_file_path_list)
        print("")

    source_path = os.path.abspath(dir1)
    backup_path = os.path.abspath(dir2)

    backup_file_path_list = []
    createdir_bool = False
    for item in diff_file_path_list:
        path_replace = item.replace(source_path, backup_path)
        backup_file_path_list.append(path_replace)
        try :
            if os.path.isdir(item):
                # os.makedirs(path_replace)
                createdir_bool = True
        except:
            pass

    if createdir_bool:
        backup_file_path_list = []
        only_files, diff_files = dir_comparison(dir1, dir2)
        for item in only_files:
            replace_path = item.replace(source_path, backup_path)
            backup_file_path_list.append(replace_path)

    if len(diff_file_path_list)>=0:
        print("###start web restore###")
        diff_replace(diff_file_path_list, backup_file_path_list)
        print("")


if __name__ == '__main__':
    # main()
    timed = input("statr auto restore，please input auto restore time:")
    while True:
        time.sleep(int(timed))
        main()
        print("=" * 70)
        only_file_path_list = []
        diff_file_path_list = []
