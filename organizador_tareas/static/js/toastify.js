export default function mostrarMensaje(mensaje, tipo) {
  if (tipo == 'éxito') {
    bgColor = "linear-gradient(to right, #00b09b, #96c93d)"
  }
  else {
    bgColor = "rgba(255 0 0 / 1)"
  }

  Toastify({
    text: mensaje,
    duration: 3000,
    destination: "https://github.com/apvarun/toastify-js",
    newWindow: true,
    close: true,
    gravity: "top", // `top` or `bottom`
    position: "left", // `left`, `center` or `right`
    stopOnFocus: true, // Prevents dismissing of toast on hover
    style: {
      background: bgColor,
    },
    onClick: function(){} // Callback after click
  }).showToast();
}
