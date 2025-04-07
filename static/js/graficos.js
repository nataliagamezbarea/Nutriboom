window.onload = function () {
    var chart = echarts.init(document.getElementById("chart"));

    // Obtener el id del usuario
    fetch("http://localhost:5000/ver_id_usuario")
        .then(response => {
            if (!response.ok) {
                throw new Error("Error al obtener el id del usuario");
            }
            return response.json();
        })
        .then(user => {
            fetch(`http://localhost:5000/estadistica/${user.id_usuario}`)
                .then(response => {
                    if (!response.ok) {
                        return null;  
                    }
                    return response.json();
                })
                .then(data => {
                    if (!Array.isArray(data) || data.length === 0) {
                        return;
                    }

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
                        var item = data.find(d => d.dia === dia); 
                        dias.push(diasTraduccion[dia]);

                        if (item) {
                            pesos.push(item.peso);
                            grasas.push(item.grasa_corporal);
                        } else {
                            pesos.push(null);
                            grasas.push(null);
                        }
                    }

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

                    chart.setOption(option);
                });
        })
        .catch(error => {
            console.error("Error al obtener el id del usuario: ", error);
        });
};
