
$(document).ready(function() {
  $("p").click(function() {
    $(this).hide();
  });

  function storeSelectedValue() {
    const radios = document.getElementsByName('optradio');
    for (const radio of radios) {
      if (radio.checked) {
        document.getElementById('selectedTrophyCount').value = radio.value;
        break;
      }
    }
    return true;
  }
});
