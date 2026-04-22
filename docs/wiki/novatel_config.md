# `Novatel Oem7 RTK config` 


To set the Novatel Oem7 to RTK config


To check the detailed log's:
```
log loglist
```

Disable logging:
```
unlogall icom1 true
```

Check the current ntrip config:
```
log ntripconfig
```


```
log interfacemode
```


```
interfacemode ncom1 auto novatel off
```



```
log ipstatus
```


```
log ncom1 gpgga ontime 5
```



```
log correctionstats
```
 