# -*- coding: utf-8 -*-

import psutil
import datetime

# 查看cpu的信息
print(u"CPU count %s" % psutil.cpu_count())
print(u"real cpu count %s" % psutil.cpu_count(logical=False))
print(psutil.cpu_times())
print(psutil.cpu_stats())
print(psutil.cpu_freq())
print(psutil.cpu_percent(interval=1, percpu=True))
print("memory")
mem = psutil.virtual_memory()
print(mem)
print(mem.available)
print(psutil.swap_memory())
print("disk")
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())
print(psutil.disk_io_counters(perdisk=True))
print()

# 系统启动时间
print(u"boot_time %s" % datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

# 系统用户
users_count = len(psutil.users())
users_list = ",".join([u.name for u in psutil.users()])
print(u"current user num %s, as %s" % (users_count, users_list))

# 网卡，可以得到网卡属性，连接数，当前流量等信息
net = psutil.net_io_counters()
bytes_sent = '{0:.2f} kb'.format(net.bytes_recv / 1024)
bytes_rcvd = '{0:.2f} kb'.format(net.bytes_sent / 1024)
print(u"receive traffic %s send traffic %s" % (bytes_rcvd, bytes_sent))

# 进程  进程的各种详细参数

