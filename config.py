# config 파일로 만들어서 놓으면 실행될때 메모리에 적재된상태로 시랳ㅇ이어서
# 노출될일이 없지만 web에서 하면 보이기떄문에 보안취약
db = {
    'user' : 'webdb',
    'password' : 'webdb',
    'host' : '192.168.1.92',
    'port' : '5432',
    'database' : 'webdb'
}