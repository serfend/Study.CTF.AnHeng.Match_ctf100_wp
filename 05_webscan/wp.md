#WebScan
#Title:允许任意文件包含
#Flag:flag{570c20dfe121a324b13ca9196c4178cf}
1题目给出了安全分析报告得出题目中包含多个洞，任意使用其中一个
2利用其中文件读取洞，读取apache配置文件../../../../../..//etc/httpd/conf/httpd.conf
3搜索字符串 flag
