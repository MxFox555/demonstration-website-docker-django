var tickPricesPlot = [];
var stabVolPlot = [];

function euroFormatter(v, axis) {
  return "$" + v.toFixed(axis.tickDecimals);
}

function dateValZip(dates, values) {
  var zipped = [];
  for (let i = 0; i < dates.length; i++) {
    zipped.push([dates[i], values[i]]);
  }
  return zipped;
}

function doPlot(position, tickerPrices, stableVolatile, convDates) {
  closePlot = dateValZip(convDates, tickerPrices['close']);
  stabPlot = dateValZip(convDates, stableVolatile['stable']);
  volPlot = dateValZip(convDates, stableVolatile['volatile']);
  $.plot($("#flot-line-chart-multi"), [{
    data: closePlot,
    label: "Close ($)",
    yaxis: 2
  }, {
    data: stabPlot,
    label: "Stable"
  }, {
    data: volPlot,
    label: "Volatile"
  }], {
    xaxes: [{
      mode: 'time'
    }],
    yaxes: [{
      min: 0
    }, {
      // align if we are to the right
      alignTicksWithAxis: position == "right" ? 1 : null,
      position: position,
      tickFormatter: euroFormatter
    }],
    legend: {
      position: 'sw'
    },
    grid: {
      hoverable: true //IMPORTANT! this is needed for tooltip to work
    },
    tooltip: true,
    tooltipOpts: {
      content: "%s for %x was %y",
      xDateFormat: "%y-%0m-%0d",

      onHover: function(flotItem, $tooltipEl) {
        // console.log(flotItem, $tooltipEl);
      }
    }

  });
}

doPlot("right", [], [], []);
var pubDict = {};

function makePlotValues(tickerPrices, stableVolatile) {
  //alert(JSON.stringify(tickerPrices.dates));
  //console.log(tickerPrices['dates']);
  var convertedDates = [];
  for (let i = 0; i < tickerPrices['dates'].length; i++) {
    var dateString = tickerPrices['dates'][i];
    var year = dateString.substring(0,4);
    var month = dateString.substring(4,6);
    var day = dateString.substring(6,8);
    convertedDates.push(new Date(year, month, day).getTime());
  }
  //console.log(convertedDates);
  //console.log(dateValZip(convertedDates, tickerPrices['high']));
  doPlot("right", tickPrices, stableVolatile, convertedDates);
  pubDict.tickPrices = tickPrices;
  pubDict.stableVolatile = stableVolatile;
  pubDict.convertedDates = convertedDates;
  console.log(pubDict);
}

function getHeaderFormat(textArr) {
  firstLine = textArr[0];
  titles = ["Ticker","Date","Open","High","Low","Close","Adj Close","Volume"];
  if (titles.indexOf(firstLine.split(',')[0]) !== -1) {
    return [true, firstLine.split(",")];
  } else {
    return [false, ["Date","Open","High","Low","Close","Adj Close","Volume"]];
  }
}

function getDictionaryValues(textArr) {
  header = getHeaderFormat(textArr);
  var body;
  if (header[0] == true) {
    body = textArr
    body.shift();
  } else {
    body = textArr;
  }
  var ticker_dict = {};
  for (let i = 0; i < header[1].length; i++) {
    ticker_dict[header[1][i]] = [];
  }
  for (let i = 0; i < header[1].length; i++) {
    for (let j = 0; j < body.length; j++) {
      splitLine = body[j].split(",");
      //console.log(splitLine);
      if (splitLine.indexOf("null") == -1) {
        if (header[1][i] == "Date") {
          ticker_dict[header[1][i]].push(splitLine[i].replaceAll("-", ""));
        } else {
          ticker_dict[header[1][i]].push(parseFloat(splitLine[i].replace(",", ".")));
        }
      }
    }
  }
  //console.log(ticker_dict.Date);
  return {'dates': ticker_dict.Date, 'open':ticker_dict.Open, 'high':ticker_dict.High, 'low':ticker_dict.Low, 'close':ticker_dict.Close, 'volume':ticker_dict.Volume}
}

function makeRequest(dictVals) {
  dictVals['key'] = document.getElementById('api-key').value;
  var xhr = new XMLHttpRequest();
  var url = window.location.protocol + '//' + window.location.hostname + ":" + window.location.port + '/api/request/';
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var json = JSON.parse(xhr.responseText);
      stabVol = json;
      if (stabVol.hasOwnProperty('error')) {
        alert(stabVol['error']);
      } else {
      //doPlot("right");
        makePlotValues(dictVals, stabVol);
      }
    }
  };
  var data = dictVals;
  //console.log(data);
  xhr.send(JSON.stringify(data));
}

$("#calculate-button").click(function() {
  var file = document.getElementById('txt-file-input').files[0];
  var FR = new FileReader();

  var fileTextArr;

  FR.readAsText(file);
  FR.onload = function(data) {
    var myVar = data.target.result;
    fileTextArr = myVar.split("\n");
    tickPrices = getDictionaryValues(fileTextArr);
    //tickDates = tickPrices.Date;
    stabVol = makeRequest(tickPrices);
  }
});
