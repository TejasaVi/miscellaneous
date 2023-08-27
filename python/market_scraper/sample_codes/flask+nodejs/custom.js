function getHello() {
	const url = 'http://localhost:9000/receiver'
	const response = fetch(url)
		.then((response) => response.json())
		.then((data) => console.log(data));
	document.getElementById("canvas").innerHTML = response;

}

function get_eod_data_chart() {
	const ctx = document.getElementById('canvas');
	new Chart(ctx, {
		type: 'bar',
		data: {
		labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
		datasets: [{
					label: '# of Votes',
					data: [12, 19, 3, 5, 2, 3],
					borderWidth: 1
				}]
		},
		options: {
			scales: {
					y: {
						beginAtZero: true
					}
			}
		}
	});
}
