$(document).ready(function() {
  $("p").click(function() {
    $(this).hide();
  });

  window.storeSelectedValue = function() {
    const radios = document.getElementsByName('optradio');
    for (const radio of radios) {
      if (radio.checked) {
        document.getElementById('selectedTrophyCount').value = radio.value;
        break;
      }
    }
    return true; 
  };
});
