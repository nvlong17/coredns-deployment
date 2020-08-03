# Rsyslog for CoreDNS

Install additional module "mmjsonparse" for log parsing in rsyslog

Usage:
```
# apt-get install rsyslog-mmjsonparse
```

After installing "mmjsonparse", we add the module to rsyslog by editing rsyslog.conf file

```
# vim /etc/rsyslog.conf
```

Insert the following line to the module loading snippet:
```
...
module(load="mmjsonparse")
...
```

Afterwards, a template for the program to parse the log to json format. Here I use the default format of coredns, get the log from journalctl, parse it and send it to Logstash 

The default format for coredns log:
 > {remote}:{port} - {>id} "{type} {class} {name} {proto} {size} {>do} {>bufsize}" {rcode} {>rflags} {rsize} {duration}

