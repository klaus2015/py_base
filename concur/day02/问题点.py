# multiprocessing 中子进程不能使用inpt()
# Pool(processes) 指定进程数量,默认根据系统自动判定 ,根据cpu内核数定
# pool.close() 功能: 关闭进程池 ,事件队列停止增加事件,但是事件还继续执行,直到所有事件执行结束为止
# pool.join() 与前面join的区别
#SMTP client session object that
# can be used to send mail to any Internet machine with
# an SMTP or ESMTP listener daemon. For details of SMTP and ESMTP
# operation, consult RFC 821 (Simple Mail Transfer Protocol) and RFC 1869
f = open('file01','rb')
n = len(f)
data = f.read(n//2)
print(data)
f.close()

# 自定义线程类