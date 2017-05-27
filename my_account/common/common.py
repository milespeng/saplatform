# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import subprocess
import sys
import logging
import time
import ConfigParser
import json


def logMsg(fun_name, err_msg, level):
    message = fun_name + ':' + err_msg
    logger = None
    logger = logging.getLogger()
    logname = sys.argv[0] + '.log'
    hdlr = logging.FileHandler(logname)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.NOTSET)
    logger.log(level, message)
    hdlr.flush()
    logger.removeHandler(hdlr)  # 网络上的实现基本为说明这条语句的使用和作用


def get_section_values(sections, filename):
    cf = ConfigParser.SafeConfigParser()
    cf.read(filename)
    configDataSection = cf.sections()
    returnData = {}

    if sections in configDataSection:
        _list = cf.items(sections)
        for _key, _value in _list:
            returnData[_key] = _value
    else:
        print "[ERROR] %s is not in config files,PLS check it %s" % (sections, filename)
        msg_info = "===%s: Get info Failed!!===" % sections
        logMsg("get_config", msg_info, 2)
        return False
    return returnData


def run_cmd(cmd):
    msg = "Starting run: %s " % cmd
    logMsg("run_cmd", msg, 1)
    cmdref = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error_info = cmdref.communicate()
    if error_info:
        if isinstance(error_info, list) or isinstance(error_info, tuple):
            error_info = error_info[0]
        msg = "RUN %s ERROR,error info:  %s" % (cmd, error_info)
        logMsg("run_cmd", msg, 2)
        return False, error_info
    else:
        msg = "run %s success" % cmd
        logMsg("cmd", msg, 1)
        # print "Run Success!!"
        return True, output


def get_cmd_out(cmd):
    import commands
    out = commands.getoutput(cmd)
    return out


def return_day(interval, base_time=time.time()):
    before = base_time - interval * 24 * 3600
    return time.strftime("%Y%m%d", time.localtime(before))


def write_file(filename, data, method='w'):
    with open(filename, method) as f:
        f.write(data)
        f.close()
    return True


def return_section(files):
    cf = ConfigParser.SafeConfigParser()
    cf.read(files)
    sections = cf.sections()
    return sections


def write_file_josn(filename, data, method='w'):
    with open(filename, method) as f:
        f.write(json.dumps(data, indent=1))
        f.close()
    return True

    # import time
    #
    # # 格式化成2016-03-20 11:45:39形式
    # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #
    # # 格式化成Sat Mar 28 22:24:24 2016形式
    # print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
    #
    # # 将格式字符串转换为时间戳
    # a = "Sat Mar 28 22:24:24 2016"
    # print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
