function CopyFromTextbox(textbox_id) {
  var copyText = document.getElementById(textbox_id);

  copyText.select();
  copyText.setSelectionRange(0, 999999);

  navigator.clipboard.writeText(copyText.value);
}
