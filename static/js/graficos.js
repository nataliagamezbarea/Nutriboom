window.onload = function () {
    var chart = echarts.init(document.getElementById("chart"));

    fetch("http://localhost:5000/estadistica/1")
        .then(response => response.json())
        .then(data => {
            var dias = [];
            var pesos = [];
            var grasas = [];

            var diasTraduccion = {
                "Monday": "Lunes",
                "Tuesday": "Martes",
                "Wednesday": "Miércoles",
                "Thursday": "Jueves",
                "Friday": "Viernes",
                "Saturday": "Sábado",
                "Sunday": "Domingo"
            };

            var diasSemana = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

            for (var i = 0; i < diasSemana.length; i++) {
                var dia = diasSemana[i];
                var item = data.find(d => d.dia === dia); // Buscamos si el día existe en los datos
                // Agregamos el día traducido a la lista
                dias.push(diasTraduccion[dia]);

                if (item) {
                    // Si encontramos el día, agregamos el peso y la grasa corporal
                    pesos.push(item.peso);
                    grasas.push(item.grasa_corporal);
                } else {
                    // Si no encontramos el día, agregamos valores nulos
                    pesos.push(null);
                    grasas.push(null);
                }
            }

            // Configuración del gráfico
            var option = {
                title: { text: "Nutriboom" },
                tooltip: {},
                legend: {
                    data: ["Peso", "Grasa Corporal"],
                    orient: "horizontal",
                    left: "center"
                },
                xAxis: {
                    data: dias
                },
                yAxis: {},
                series: [
                    {
                        name: "Peso",
                        type: "line",
                        data: pesos,
                        itemStyle: { color: "blue" }
                    },
                    {
                        name: "Grasa Corporal",
                        type: "line",
                        data: grasas,
                        itemStyle: { color: "red" }
                    }
                ]
            };

            // Mostrar el gráfico con los datos configurados
            chart.setOption(option);
        })
        .catch(error => console.error("Error al obtener los datos: ", error));
};
