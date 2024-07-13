function iniciarMap() {
  var coord = {lat: -33.5868269, lng: -70.5799867};
  var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 15,
      center: coord
  });
  var marker = new google.maps.Marker({
      position: coord,
      map: map
  });
}

document.addEventListener('DOMContentLoaded', function() {
  // Función para obtener datos del dólar desde la API de Mindicador
  function getDolar(done) {
      fetch("https://www.mindicador.cl/api/dolar")
          .then((response) => {
              if (!response.ok) {
                  throw new Error("Network response was not ok");
              }
              return response.json();
          })
          .then((data) => {
              // Llama a la función 'done' con los datos requeridos
              done(data.serie[0]); // Tomamos el primer elemento del array 'serie'
          })
          .catch((error) => {
              console.error('Error fetching data:', error);
          });
  }

  // Función para renderizar los datos del dólar en el template
  function renderDolar(dolarData) {
      // Actualizar los elementos en el DOM con los datos del dólar
      const fechaElement = document.querySelector('#dolarTemplate .fecha');
      const valorElement = document.querySelector('#dolarTemplate .valor');

      fechaElement.textContent = new Date(dolarData.fecha).toLocaleDateString();
      valorElement.textContent = dolarData.valor;
  }

  // Llamar a la función para obtener y renderizar los datos del dólar
  getDolar(renderDolar);

  // Función para obtener datos del Euro desde la API de Mindicador
  function getEuro(done) {
      fetch("https://www.mindicador.cl/api/euro")
          .then((response) => {
              if (!response.ok) {
                  throw new Error("Network response was not ok");
              }
              return response.json();
          })
          .then((data) => {
              // Llama a la función 'done' con los datos requeridos
              done(data.serie[0].fecha, data.serie[0].valor); // Pasamos fecha y valor
          })
          .catch((error) => {
              console.error('Error fetching Euro data:', error);
          });
  }

  // Función para renderizar los datos del Euro en el template
  function renderEuro(fecha, valor) {
      const valorEuroElement = document.getElementById('valorEuro');
      const fechaEuroElement = document.querySelector('#euroTemplate .fecha');
      
      fechaEuroElement.textContent = new Date(fecha).toLocaleDateString();
      valorEuroElement.textContent = valor;
  }

  // Llamar a la función para obtener y renderizar los datos del Euro
  getEuro(renderEuro);

  // Función para obtener los datos del Bitcoin desde la API de Mindicador
  function getBitcoin(done) {
      fetch("https://www.mindicador.cl/api/bitcoin")
          .then((response) => {
              if (!response.ok) {
                  throw new Error("Network response was not ok");
              }
              return response.json();
          })
          .then((data) => {
              // Llama a la función 'done' con los datos requeridos
              done(data.serie[0].fecha, data.serie[0].valor); // Pasamos fecha y valor
          })
          .catch((error) => {
              console.error('Error fetching Bitcoin data:', error);
          });
  }

  // Función para renderizar los datos del Bitcoin en el template
  function renderBitcoin(fecha, valor) {
      const valorBitcoinElement = document.getElementById('valorBitcoin');
      const fechaBitcoinElement = document.querySelector('#bitcoinTemplate .fecha');
      
      fechaBitcoinElement.textContent = new Date(fecha).toLocaleDateString();
      valorBitcoinElement.textContent = valor;
  }

  // Llamar a la función para obtener y renderizar los datos del Bitcoin
  getBitcoin(renderBitcoin);
});
