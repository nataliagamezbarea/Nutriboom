window.onload = async function () {
    const contenedorGrafico = document.getElementById("chart");

    const diasTraduccion = {
        "Monday": "Lunes",
        "Tuesday": "Martes",
        "Wednesday": "Miércoles",
        "Thursday": "Jueves",
        "Friday": "Viernes",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    };

    const diasSemana = Object.keys(diasTraduccion);

    // 1. Obtener ID del usuario
    const respuestaUsuario = await fetch("http://localhost:5000/ver_id_usuario");
    const usuario = await respuestaUsuario.json();

    // 2. Obtener datos estadísticos
    const respuestaEstadisticas = await fetch(`http://localhost:5000/estadistica/${usuario.id_usuario}`);
    const datos = await respuestaEstadisticas.json();

    // Verificar si datos es un arreglo y contiene datos
    if (!Array.isArray(datos) || datos.length === 0) {
        // Si no hay datos, mostrar mensaje sin gráfico
        contenedorGrafico.innerHTML = "<h2>No tienes datos diarias, por favor registra datos</h2>";
    } else {
        // Si hay datos, mostrar gráfico
        const grafico = echarts.init(contenedorGrafico);

        // 3. Organizar datos
        const dias = [];
        const pesos = [];
        const grasas = [];

        diasSemana.forEach(dia => {
            const item = datos.find(d => d.dia === dia);
            dias.push(diasTraduccion[dia]);
            pesos.push(item ? item.peso : null);
            grasas.push(item ? item.grasa_corporal : null);
        });

        // 4. Configurar y mostrar gráfico
        const opcion = {
            title: { text: "Nutriboom" },
            tooltip: {},
            legend: {
                data: ["Peso", "Grasa Corporal"],
                orient: "horizontal",
                left: "center"
            },
            xAxis: { data: dias },
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

        grafico.setOption(opcion);
    }
};
