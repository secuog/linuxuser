import os
import re


def logindefs():
    with open('/etc/login.defs') as file:
        line_list = file.readlines()
        pattern = f"\\#PASS_MIN_LEN\s*|^PASS_MIN_LEN\s*"
        for line in line_list:
            if re.match(pattern, line):
                print(line)
                if re.match('#PASS_MIN_LEN\s*', line):
                    print('最短密码限制已被注释')
                    user_input = input("是否修改最短密码限制： y/n")
                    index = line_list.index(line)
                    if user_input == "y":
                        value2 = input("输入最短密码限制要设置的值")
                        line_list[index] = f"PASS_MIN_LEN {value2}\n"
                        content = ''.join(line_list)
                        with open('./test.defs', 'w') as f:
                            f.writelines(line_list)
                        print(f"第{index}行 PASS_MIN_LEN 已修改为{value2}")
                    else:
                        pass
                else:
                    index = line_list.index(line)
                    value = line.split(' ')[1].strip()
                    if value >= '12':
                        print(f'最短密码限制为{value} 安全')
                    else:
                        print(f'最短密码限制为{value} 建议修改为12以上')
                        user_input = input("是否修改最短密码限制： y/n")
                        if user_input == "y":
                            value2 = input("输入最短密码限制要设置的值")
                            line_list[index] = f"PASS_MIN_LEN {value2}\n"
                            content = ''.join(line_list)
                            with open('./test.defs', 'w') as f:
                                f.writelines(line_list)
                            print(f"第{index}行 PASS_MIN_LEN 已修改为{value2}")
                        else:
                            pass
    with open('./test.defs') as file:
        line_list = file.readlines()
        pattern = f"\\#PASS_MAX_DAYS\s*|^PASS_MAX_DAYS\s*"
        for line in line_list:
            if re.match(pattern, line):
                print(line)
                if re.match('#PASS_MAX_DAYS\s*', line):
                    print('用户密码最长使用天数已被注释')
                    user_input = input("是否修改用户密码最长使用天数： y/n")
                    index = line_list.index(line)
                    if user_input == "y":
                        value2 = input("输入用户密码最长使用天数要设置的值")
                        line_list[index] = f"PASS_MAX_DAYS {value2}\n"
                        content = ''.join(line_list)
                        with open('./test.defs', 'w') as f:
                            f.writelines(line_list)
                        print(f"第{index}行 PASS_MAX_DAYS 已修改为{value2}")
                    else:
                        pass
                else:
                    index = line_list.index(line)
                    value = line.split(' ')[1].strip()
                    if value >= '90':
                        print(f'用户密码最长使用天数为{value} 安全')
                    else:
                        print(f'用户密码最长使用天数为{value} 建议修改为90以上')
                        user_input = input("是否修改最短密码限制： y/n")
                        if user_input == "y":
                            value2 = input("输入用户密码最长使用天数要设置的值")
                            line_list[index] = f"PASS_MAX_DAYS {value2}\n"
                            content = ''.join(line_list)
                            with open('./test.defs', 'w') as f:
                                f.writelines(line_list)
                            print(f"第{index}行 PASS_MAX_DAYS 已修改为{value2}")
                        else:
                            pass
def sysauth():
    with open('/etc/pam.d/system-auth') as file:
        line_list = file.readlines()
        pattern = f"^passwd requisite pam_cracklib.so\s*"
        for line in line_list:
            index = line_list.index(line)
            if re.match(pattern, line):
                str_list = line.split(" ")
                result_dict = {}
                for item in str_list:
                    if "=" in item:
                        key, value = item.split("=")
                        result_dict[key] = value
                if 'retry' in result_dict:
                    print('尝试次数为 ' + result_dict['retry'])
                    user_input = input("是否修改： y/n")
                    if user_input == "y":
                        value2 = input("输入要设置的值")
                        result_dict['retry'] = value2
                        print('尝试次数修改为 ' + result_dict['retry'])
                    print('____________________________________')
                if 'difok' in result_dict:
                    print('最少不同字符为 ' + result_dict['difok'])
                    user_input = input("是否修改： y/n")
                    if user_input == "y":
                        value2 = input("输入要设置的值")
                        result_dict['difok'] = value2
                        print('最少不同字符修改为 ' + result_dict['difok'])
                    print('____________________________________')
                if 'ucredit' in result_dict:
                    print('最少大写字母为 ' + result_dict['ucredit'])
                    user_input = input("是否修改： y/n")
                    if user_input == "y":
                        value2 = input("输入要设置的值")
                        result_dict['ucredit'] = value2
                        print('最少大写字母修改为 ' + result_dict['ucredit'])
                    print('____________________________________')
                if 'lcredit' in result_dict:
                    print('最少小写字母为 ' + result_dict['lcredit'])
                    user_input = input("是否修改： y/n")
                    if user_input == "y":
                        value2 = input("输入要设置的值")
                        result_dict['lcredit'] = value2
                        print('最少小写字母修改为 ' + result_dict['lcredit'])
                    print('____________________________________')
                if 'dcredit' in result_dict:
                    print('最少数字为 ' + result_dict['dcredit'])
                    user_input = input("是否修改： y/n")
                    if user_input == "y":
                        value2 = input("输入要设置的值")
                        result_dict['dcredit'] = value2
                        print('最少数字修改为 ' + result_dict['dcredit'])
                    print('____________________________________')
                result_list = []
                for key, value in result_dict.items():
                    result_list.append(f"{key}={value}")
                result_str = ", ".join(result_list)
                result_str = result_str.replace(',', '')
                line_list[index] = f"passwd requisite pam_cracklib.so {result_str}"
                with open('./test.defs', 'w') as f:
                    f.writelines(line_list)
                print(f"第{index}行 密码策略修改已保存")
def sysauth1():
    with open('/etc/pam.d/system-auth') as file:
        line_list = file.readlines()
        pattern = f"^auth required pam.tally.so\s*"
        for line in line_list:
            index = line_list.index(line)
            if re.match(pattern, line):
                if 'even_deny_root' in line:
                    delimiter = "even_deny_root"
                    list1, list2 = line.split(delimiter)
                    list2 = delimiter + list2
                    str_list1 = list1.split(" ")
                    result_dict1 = {}
                    str_list2 = list2.split(" ")
                    result_dict2 = {}
                    print(str_list1, str_list2)
                    for item in str_list1:
                        if "=" in item:
                            key, value = item.split("=")
                            result_dict1[key] = value
                    for item in str_list2:
                        if "=" in item:
                            key, value = item.split("=")
                            result_dict2[key] = value
                    if 'onerr' in result_dict1:
                        if 'deny' in result_dict1:
                            print('连续登陆失败次数次数为 ' + result_dict1['deny'])
                            user_input = input("是否修改： y/n")
                            if user_input == "y":
                                value2 = input("输入要设置的值")
                                result_dict1['deny'] = value2
                                print('连续登陆失败次数修改为 ' + result_dict1['deny'])
                    print('____________________________________')
                    if 'unlock_time' in result_dict1:
                        print('普通用户锁定登陆时间 ' + result_dict1['unlock_time'])
                    user_input = input("是否修改： y/n")
                    if user_input == "y":
                        value2 = input("输入要设置的值")
                        result_dict1['unlock_time'] = value2
                        print('普通用户锁定登陆时间修改为' + result_dict1['unlock_time'])
                    print('____________________________________')
                    if 'root_unlock_time' in result_dict2:
                        print('root用户锁定登陆时间 ' + result_dict2['root_unlock_time'])
                        user_input = input("是否修改： y/n")
                        if user_input == "y":
                            value2 = input("输入要设置的值")
                            result_dict2['root_unlock_time'] = value2
                            print('root用户锁定登陆时间修改为' + result_dict2['root_unlock_time'])
                        print('____________________________________')
                    result_list1 = []
                    for key, value in result_dict1.items():
                        result_list1.append(f"{key}={value}")
                    result_str1 = ", ".join(result_list1)
                    result_str1 = result_str1.replace(',', '')
                    result_list2 = []
                    for key, value in result_dict2.items():
                        result_list2.append(f"{key}={value}")
                        result_str2 = ", ".join(result_list2)
                        result_str2 = result_str2.replace(',', '')
                    line_list[index] = f"auth required pam.tally.so {result_str1} even_deny_root {result_str2}"
                    with open('./test.defs', 'w') as f:
                        f.writelines(line_list)
                    print(f"第{index}行 密码策略修改已保存")
def tmout():
    print("终端超时设置")
    os.system("echo 'export TMOUT=600' >> /etc/profile")

if __name__ == '__main__':
    logindefs()
    print('____________________________________')
    sysauth()
    print('____________________________________')
    sysauth1()
    print('____________________________________')
    tmout()
    print('____________________________________')
