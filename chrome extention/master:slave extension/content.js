var XHR = new XMLHttpRequest();
var url = "liveloadbalancer-460709075.ap-south-1.elb.amazonaws.com/service";
var arr = [];
var names = [];
var lat,long;

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    console.log("Geolocation is not supported by this browser.");
  }
}

function showPosition(position) {
   lat=position.coords.latitude;
   long=position.coords.longitude;
}

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    var isFraud;

    body = document.querySelector(".gs").innerText;
    XHR.onreadystatechange = function () {
        if (XHR.readyState == 4) {
            if (XHR.status == 200) {
                isFraud = String(XHR.response);
                alert(isFraud === "true\n" ? "This is a fraud email" : "This is not a fraud email");
                if (isFraud) {
                    chrome.storage.local.set({ "key": arr = arr.concat([[String(isFraud), String(document.querySelector(".gD").innerText)]]) }, function () {
                        console.log("WORKING");
                    });
                    chrome.storage.local.get("key", function (data) {
                        console.log(data);
                    })
                }
                if (isFraud === "true\n"){
                    XHR.onreadystatechange = function () {
                        if (XHR.readyState == 4) {
                            if (XHR.status == 200) {
                            
                            }
                        }
                    var nXHR = new XMLHttpRequest();
                    nXHR.open("POST", "https://fraudmap.herokuapp.com/add", true);
                    nXHR.setRequestHeader("Content-type", "application/json");
                    nXHR.send(JSON.stringify({ 'lat': Float64(lat), 'lon': Float64(long) }))};
                }
            } else {
                console.log(XHR.status);
            }
        }
    }

    XHR.open("POST", url, true);
    XHR.setRequestHeader("Content-type", "application/json");
    console.log(body);
    XHR.send(JSON.stringify({ 'body': String(body) }));

    sendResponse({ isFraud: isFraud === "true\n" ? "This is a fraud email" : "This is not a fraud email" });
})

document.body.onload = function () {
    chrome.storage.local.get("key", function (data) {
        console.log(data);
        // console.log(typeof((Object.values(data))));
        a = data.key;
        var temp = ((Object.values(data))[0]);
        n = temp.length;

        for (var i = 0; i < n; i++) {
            if (temp[i][0] === "true\n") {
                names.push(temp[i][1]);
            }
        }
        // table = document.querySelector(".F")
        console.log(names);
        table = document.getElementById(":2s");
        console.log(table);
        rows = table.querySelectorAll(".zA");
        rows.forEach(function (row) {
            if(row.querySelector(".yP")) {
                if(String(row.querySelector(".yP").innerText) === names[0]) {
                    row.style.color = "red";
                }
            }
        })
    })
    getLocation();
}

