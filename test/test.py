import subprocess as sp

if __name__ == '__main__':
    cmd = "ping -n 3 -w 3 111.155.116.221"
    #执行命令
    p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    #获得返回结果并解码
    out = p.stdout.read().decode("gbk")
    print(out)