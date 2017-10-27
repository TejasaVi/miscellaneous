#!/usr/bin/python

import pprint
import argparse
import os
import json
import yaml

CFG_FILE = ""
STD_CFG = "tmp_cfg2"
IGNORE_DIRECTIVE_LIST = ("AcceptEnv", "Subsystem", "HostKey", "HostkeyAlgorithms")

def IsComment(line):
    if len(line) > 0:
        return not line[0] == "#"
    return True

def IsNotRequired(line):
    if len(line) > 0:
        return not line.startswith(IGNORE_DIRECTIVE_LIST)
    return True

def lwt(line):
    if len(line.split()) > 2 and '#' in ' '.join(line.split()[2:]):
        return line.split()[:2]
    return line.split()

def NormalizeSpaces(lines):
    new_lines = []
    for line in lines:
        new_lines.append(' '.join(line.split()))
    return new_lines

def get_config_dict(cfg_file):
    if (not os.path.exists(cfg_file)):
        print("Configuration File does not exists.")
        exit(-1)
    try:
        _file_fd = open(cfg_file, "r")
        _file_content = _file_fd.read().splitlines()
        _file_fd.close()
    except IOError, OSError:
        print("Failed to read the configuration file.\n")
        exit(-1)
    _file_content = NormalizeSpaces(_file_content)
    _file_content = filter(None,_file_content)
    _file_content = filter(IsComment,_file_content)
    _file_content = filter(IsNotRequired,_file_content)
    cfg_dict = {}
    for line in _file_content:
        key, value = lwt(line)
        if not cfg_dict.has_key(key):
            cfg_dict[key] = (value)
        else:
            orig_value = cfg_dict[key]
            if isinstance(orig_value,type([])):
                cfg_dict[key].append(value)
            else:
                cfg_dict[key] = [orig_value]
                cfg_dict[key] += [value]
    # pprint.pprint(cfg_dict)
    return cfg_dict

def dict_diff(std_cfg, cur_cfg):
    result = {}
    for key in std_cfg:
        if not cur_cfg.has_key(key):
            result[key] = std_cfg[key]
        else:
            # key is present, Check if values are same
            if not std_cfg[key] == cur_cfg[key]:
                result[key] = std_cfg[key]
    return result

def IsAudited():
    return os.path.exists('ssh-failure-audit.json')

def audit(CFG_FILE):
    cur_cfg = get_config_dict(CFG_FILE)
    std_cfg = get_config_dict(STD_CFG)
    diff_cfg = dict_diff(std_cfg, cur_cfg)
    fd = open('ssh-failure-audit.json', "w")
    json.dump(diff_cfg, fd)
    fd.close()

def secure_config(CFG_FILE):
    #import pdb;pdb.set_trace()
    json_data=open('ssh-failure-audit.json').read()
    data = json.loads(json_data)
    #data = yaml.safe_load(data)
    cur_cfg = get_config_dict(CFG_FILE)
    for key in data:
        cur_cfg[key] = data[key]
    pprint.pprint(cur_cfg)
    with open('new_config', 'w') as fd:
        for key, value in cur_cfg.items():
            fd.write('{0} {1}\n'.format(key, value))
    return cur_cfg

def runner(args):
    CFG_FILE = args.file
    if args.secure:
        if IsAudited():
            secure_config(CFG_FILE)
        else:
            audit(CFG_FILE)
            secure_config(CFG_FILE)
    else:
        audit(CFG_FILE)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SSH Configuration checker.")
    parser.add_argument('-f', '--file', help="ssh configuration file to check")
    parser.add_argument('-s', '--secure', action='store_true', help="secure ssh configuration file")
    args = parser.parse_args()
    runner(args)
