//const URL = "http://127.0.0.1:5000/"
const URL = "https://codoacodogrupo3.pythonanywhere.com/"

const app = Vue.createApp({
    data() {
        return {
            socios: []
        }
    },
    methods: {
        obtenerSocios() {
            fetch(URL + 'socios')
                .then(response => {
                    // Parseamos la respuesta JSON
                    if (response.ok) { return response.json(); }
                })
                .then(data => {
                    // El código Vue itera este elemento para generar la tabla
                    this.socios = data;
                })
                .catch(error => {
                    console.log('Error:', error);
                    alert('Error al obtener los socios.');
                });
        },
        eliminarSocio(dni) {
            if (confirm('¿Estás seguro de que quieres eliminar este socio?')) {
                fetch(URL + `socios/${dni}`, { method: 'DELETE' })
                    .then(response => {
                        if (response.ok) {
                            this.socios =
this.socios.filter(socio => socio.dni !== dni);
                            alert('Socio eliminado correctamente.');
                        }
                    })
                    .catch(error => {
                        alert(error.message);
                    });
            }
    }
},
mounted() {
    //Al cargar la página, obtenemos la lista de socios
    this.obtenerSocios();
    }
});
app.mount('body');
