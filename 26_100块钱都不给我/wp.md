flag{fc4e4034aafc11936d9a099c1867a355}

直接访问网址/?ctf=phpinfo得flag

详细步骤：
网站访问robots.txt，发现robots.txt里显示
User-agent: *
Disallow: /index.php1
打开这个PHP页面，发现可控变量$a = isset($_GET['ctf']) ? $_GET['ctf'] : '';
知道是一个PHP程序，构造一个phpinfo
访问网址/?ctf=phpinfo