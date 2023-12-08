 //const URL = "http://127.0.0.1:5000/";
const URL = "https://codoacodogrupo3.pythonanywhere.com/"

const app = Vue.createApp({
    data() {
        return {
            socios: []
        };
    },
    methods: {
        obtenerSocios() {
            fetch(URL + 'socios')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Error al obtener los socios.');
                    }
                    return response.json();
                })
                .then(data => {
                    this.socios = data;
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Error al obtener los socios.');
                });
        },
        eliminarSocios(dni) {
            if (confirm('¿Estás seguro de que quieres eliminar este socio?')) {
                fetch(URL + `socios/${dni}`, { method: 'DELETE' })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(`Error al eliminar el socio: ${response.statusText}`);
                        }
                        return response.json();
                    })
                    .then(data => {
                        this.socios = this.socios.filter(socio => socio.dni !== dni);
                        alert('Socio eliminado correctamente.');
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        alert(error.message);
                    });
            }
        }
    },
    mounted() {
        this.obtenerSocios();
    }
});

app.mount('body');