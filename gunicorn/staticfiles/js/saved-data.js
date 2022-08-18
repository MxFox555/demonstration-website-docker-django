$("#calculate-button-pcd").click(function() {
  var file = document.getElementById('txt-file-input-pcd').files[0];
  var FR = new FileReader();

  var fileTextArr;

  FR.readAsText(file);
  FR.onload = function(data) {
    var myVar = data.target.result;
    pubDict = JSON.parse(myVar);
    doPlot("right", pubDict.tickPrices, pubDict.stableVolatile, pubDict.convertedDates);
  }
});
