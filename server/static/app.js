function getBathValue() {
	let uiBathrooms = document.getElementsByName("uiBathrooms");
	for (let i in uiBathrooms) {
		if (uiBathrooms[i].checked) {
			return parseInt(i) + 1;
		}
	}
	return -1; // Invalid Value
}

function getBHKValue() {
	let uiBHK = document.getElementsByName("uiBHK");
	for (let i in uiBHK) {
		if (uiBHK[i].checked) {
			return parseInt(i) + 1;
		}
	}
	return -1; // Invalid Value
}

function getBalconyValue() {
	let uiBalcony = document.getElementsByName("uiBalcony");
	for (let i in uiBalcony) {
		if (uiBalcony[i].checked) {
			return parseInt(i);
		}
	}
	return -1; // Invalid Value
}

function onClickedEstimatePrice() {
	console.log("Estimate price button clicked");
	let sqft = document.getElementById("uiSqft");
	let bhk = getBHKValue();
	let bathrooms = getBathValue();
	let location = document.getElementById("uiLocations");
	let estPrice = document.getElementById("uiEstimatedPrice");
	let balcony = getBalconyValue();

	// let url = "/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
	let url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

	$.post(
		url,
		{
			total_sqft: parseFloat(sqft.value),
			bhk: bhk,
			bath: bathrooms,
			location: location.value,
			balcony: balcony,
		},
		function (data, status) {
			console.log(data.estimated_price);
			estPrice.innerHTML =
				"<h2>" + data.estimated_price.toString() + " Lakh</h2>";
			console.log(status);
		}
	);
}

function onPageLoad() {
	console.log("document loaded");
	// let url = "/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
	let url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
	$.get(url, function (data, status) {
		console.log("got response for get_location_names request");
		console.log(data);
		if (data) {
			let locations = data.locations;
			let uiLocations = document.getElementById("uiLocations");
			$("#uiLocations").empty();
			for (let i in locations) {
				let opt = new Option(
					locations[i].at(0).toUpperCase() + locations[i].substr(1),
					locations[i]
				);
				$("#uiLocations").append(opt);
			}
		}
	});
}

window.onload = onPageLoad;
