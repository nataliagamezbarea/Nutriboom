
function checkAll(checkboxall) {
  // selecciona todos los checkbox excepto select all que es el checkbox que selecciona todo 
  const checkboxes = document.querySelectorAll(
    'input[type="checkbox"]:not(#selectAll)'
  );

  // haz un for que recorra todas las casillas y se pongan como el select all para que asi coincidan
  checkboxes.forEach(function (checkbox) {
    checkbox.checked = checkboxall.checked;
  });
}
