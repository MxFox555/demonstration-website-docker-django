function CheckPassword(one_input, two_input, password_wrapper, error_message, submit_btn) {

  var input1 = document.getElementsByName(one_input)[0];
  var input2 = document.getElementsByName(two_input)[0];
  var pw_wrapper = document.getElementsByName(password_wrapper)[0];
  var err_msg = document.getElementsByName(error_message)[0];
  var sub_btn = document.getElementsByName(submit_btn)[0];

  if (input1.value != input2.value) {
    err_msg.hidden = false;
    pw_wrapper.classList.add('has-error');
    sub_btn.classList.add('disabled');
  } else {
    err_msg.hidden = true;
    pw_wrapper.classList.remove('has-error');
    sub_btn.classList.remove('disabled');
  }
}
