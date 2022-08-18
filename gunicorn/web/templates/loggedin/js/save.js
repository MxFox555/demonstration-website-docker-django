$("#save-button").click(function() {
  if (pubDict !== []) {
    var hiddenElement = document.createElement('a');

    hiddenElement.href = 'data:attachment/text,' + encodeURI(JSON.stringify(pubDict));
    hiddenElement.target = '_blank';
    hiddenElement.download = document.getElementById("txt-file-input").value.split(/(\\|\/)/g).pop().split('.')[0] + '.simfile';
    hiddenElement.click();
  } else {
    alert('There is no data to save.');
  }
});
