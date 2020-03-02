window.onload = function () {
    chrome.storage.local.get("key", function (data) {
        true_percent = 0
        false_percent = 0
        a = data.key;
        var temp = ((Object.values(data))[0]);
        n = temp.length;
        for (var i = 0; i < n; i++) {
            if (temp[i][0] === "true\n") {
                false_percent++;
            }
            else true_percent++;
        }
        true_percent = 100-37.12
        false_percent = 37.12
        var chart = new CanvasJS.Chart("chartContainer", {
            animationEnabled: true,
            title: {
                text: "Out of the mails you receive:"
            },
            data: [{
                type: "pie",
                startAngle: 240,
                yValueFormatString: "##0.00\"%\"",
                indexLabel: "{label} {y}",
                dataPoints: [
                    { y: true_percent, label: "Not Fraud" },
                    { y: false_percent, label: "Fraud" }
                    
                ]
            }]
        });
        chart.render();
    });

}