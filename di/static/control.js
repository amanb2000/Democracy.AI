function download(ID) {
	$.post('/downloadML',   // url
		{
			'ID': ID // data to be submit
		},
		function(data) {// success callback
			console.log("Data: " + data);
		}
	);
}

function vote(ID, value) {
	$.post('/voteML',   // url
		{
			'ID': ID,
			'value': value
		}, // data to be submit
		function(data) {// success callback
			console.log("Data: " + data);
		}
	);
}

function save(ID) {
	$.post('/bookmarkML',   // url
		{
			'ID': ID,
		}, // data to be submit
		function(data) {// success callback
			console.log("Data: " + data);
		}
	);
}

function report(ID) {
	$.post('/reportML',   // url
		{
			'ID': ID,
		}, // data to be submit
		function(data) {// success callback
			console.log("Data: " + data);
		}
	);
}
