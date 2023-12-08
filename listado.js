// const URL = "http://127.0.0.1:5000/"
const URL = "https://codoacodogrupo3.pythonanywhere.com/"

// Realizamos la solicitud GET al servidor para obtener todos los socios
fetch(URL + 'socios')
    .then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
                // Si hubo un error, lanzar explícitamente una excepción
                // para ser "catcheada" más adelante
                throw new Error('Error al obtener los socios.');
            }
        })
        .then(function (data) {
            let tablaSocios = document.getElementById('tablaSocios');
            // Iteramos sobre los socios y agregamos filas a la tabla
            for (let socio of data) {
                let fila = document.createElement('tr');
                fila.innerHTML = '<td>' + socio.dni + '</td>' +
                    '<td>' + socio.apellido + '</td>' +
                    '<td align="right">' + socio.nombre + '</td>' +
                    '<td align="right">' + socio.edad + '</td>' +
                    '<td align="right">' + socio.plan + '</td>';
            //Una vez que se crea la fila con el contenido del socio,se agrega a la tabla utilizando el método appendChild del elemento tablaSocios.
                tablaSocios.appendChild(fila);
            }
        })
        .catch(function (error) {
            // En caso de error
            alert('Error al agregar el socio.');
            console.error('Error:', error);
            }) 