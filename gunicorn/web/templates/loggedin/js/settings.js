function OnCheckDeleteAcc(checkbox_id, button_id) {
  var button_obj = document.getElementById(button_id);
  var checkbox_obj = document.getElementById(checkbox_id);

  if (checkbox_obj.checked) {
    button_obj.classList.remove('disabled');
  }else {
    button_obj.classList.add('disabled');
  }
}
