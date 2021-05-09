$.ready(function() {
    $("#crearform").validate({
        rules: {
            nombre: {
                required = true,
                maxlength = 100
            },
            descripcion: {
                required = true,
                maxlength = 220
            },

        },
        messages: {
            nombre: {
                required = "Se necesita el campo",
                maxlength = "Se necesita minimo 5"
            },
            descripcion: {
                required = "Se necesita el campo",
                maxlength = "Se necesita minimo 10"
            },
        }
    });
});