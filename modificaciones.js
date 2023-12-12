//const URL = "http://127.0.0.1:5000/"
 const URL = "https://codoacodogrupo3.pythonanywhere.com/"

const app = Vue.createApp({
    data() {
        return {
            dni: '',
            apellido: '',
            nombre: '',
            edad: '',
            plan: '',
            mostrarDatosSocio: false,
        };
    },

    methods: {
        obtenerSocio() {
            fetch(URL + 'socios/' + this.dni)
                .then(response => {
                    if (response.ok) {
                        return response.json()
                    } else {
                        //Si la respuesta es un error, lanzamos una excepción para ser "catcheada" más adelante en el catch.
                        throw new Error('Error al obtener los datos del socio.')
                    }
               })

                .then(data => {
                    this.apellido = data.apellido;
                    this.nombre = data.nombre;
                    this.edad = data.edad;
                    this.plan = data.plan;
                    this.mostrarDatosSocio = true;
                })
                .catch(error => {
                    console.log(error);
                    alert('DNI no encontrado.');
                })
    },
        guardarCambios() {
            const formData = new FormData();
            formData.append('dni', this.dni);
            formData.append('apellido', this.apellido);
            formData.append('nombre', this.nombre);
            formData.append('edad', this.edad);
            formData.append('plan', this.plan);
        //Utilizamos fetch para realizar una solicitud PUT a la API y guardar los cambios.
            fetch(URL + 'socios/' + this.dni, {
                method: 'PUT',
                body: formData,
            })
            .then(response => {
        //Si la respuesta es exitosa, utilizamos response.json para parsear la respuesta en formato JSON.
                if (response.ok) {
                    return response.json()
                } else {
        //Si la respuesta es un error, lanzamos una excepción.
                    throw new Error('Error al guardar los cambios del socio.')
                }
            })
            .then(data => {
                alert('Producto actualizado correctamente.');
                this.limpiarFormulario();
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al actualizar el socio.');
            });
        },
        limpiarFormulario() {
            this.dni = '';
            this.apellido = '';
            this.nombre = '';
            this.edad = '';
            this.plan = '';
            this.mostrarDatosSocio = false;
        }
    }    
});
    app.mount('#app');
    
