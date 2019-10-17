#web1
#Title:cookies异常
#flag:flag{1284dc540c427d9b02ef5e0956e95489}
#code:main.py

1通过尝试任意注册发现cookies的uid和username是base64编码
2通过观察发现uid位数未发生过变化，从而推断出uid可能代表某种权限
3尝试用AES算法匹配，填充一个区块，16位+1得到username的54后位
4填入uid得到flag


```HTML
                    <p>
                                                    <span>Hi aaaaaaserfend0006. </span>
                                                            <span>(Administrator)</span><br>
                                    flag{1284dc540c427d9b02ef5e0956e95489}
                                 </p>

```