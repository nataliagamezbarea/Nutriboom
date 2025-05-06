window.onload = async function () {
  const contenedorGrafico = document.getElementById("chart");

  const diasTraduccion = {
    Monday: "Lunes",
    Tuesday: "Martes",
    Wednesday: "Miércoles",
    Thursday: "Jueves",
    Friday: "Viernes",
    Saturday: "Sábado",
    Sunday: "Domingo",
  };

  const diasSemana = Object.keys(diasTraduccion);

  // 1. Obtener ID del usuario
  const respuestaUsuario = await fetch("http://localhost:5000/ver_id_usuario");
  const usuario = await respuestaUsuario.json();

  // 2. Obtener datos estadísticos
  const respuestaestadistica_generals = await fetch(
    `http://localhost:5000/estadistica_general/${usuario.id_usuario}`
  );
  const datos = await respuestaestadistica_generals.json();

  // Verificar si datos es un arreglo y contiene datos
  if (!Array.isArray(datos) || datos.length === 0) {
    // Si no hay datos, mostrar mensaje sin gráfico
    contenedorGrafico.innerHTML =
      "<h2>No tienes datos diarias, por favor registra datos</h2>";
  } else {
    // Si hay datos, mostrar gráfico
    const grafico = echarts.init(contenedorGrafico);

    // 3. Organizar datos
    const dias = [];
    const pesos = [];
    const grasas = [];

    diasSemana.forEach((dia) => {
      const item = datos.find((d) => d.dia === dia);
      dias.push(diasTraduccion[dia]);
      pesos.push(item ? item.peso : null);
      grasas.push(item ? item.grasa_corporal : null);
    });

    // 4. Configurar y mostrar gráfico
    const opcion = {
      title: {
        left: "center",
        textStyle: {
          fontSize: 24,
          fontWeight: 'bold',
          color: '#333',
        },
        subtextStyle: {
          fontSize: 14,
          color: '#666',
        },
      },
      tooltip: {
        trigger: 'axis',
      },
      legend: {
        data: ["Peso", "Grasa Corporal"],
        orient: "horizontal",
        left: "center",
        textStyle: {
          fontSize: 16,
          color: '#333',
        },
      },
      grid: {
        left: '5%',
        right: '5%',
        bottom: '10%',
        top: '20%',
      },
      xAxis: {
        type: "category",
        data: dias,
        axisLabel: {
          fontSize: 14,
          color: "#333",
        },
        axisLine: {
          lineStyle: {
            color: "#ccc",
          },
        },
      },
      yAxis: {
        type: "value",
        axisLabel: {
          fontSize: 14,
          color: "#333",
        },
        axisLine: {
          lineStyle: {
            color: "#ccc",
          },
        },
      },
      series: [
        {
          name: "Peso",
          type: "line",
          data: pesos,
          itemStyle: {
            color: "#4e92d8",
            borderWidth: 3,
            borderColor: "#1c6db2",
          },
          lineStyle: {
            width: 4,
            type: 'solid',
          },
          smooth: true,
          symbol: 'circle',
          symbolSize: 8,
        },
        {
          name: "Grasa Corporal",
          type: "line",
          data: grasas,
          itemStyle: {
            color: "#e74c3c",
            borderWidth: 3,
            borderColor: "#c0392b",
          },
          lineStyle: {
            width: 4,
            type: 'solid',
          },
          smooth: true,
          symbol: 'circle',
          symbolSize: 8,
        },
      ],
      animationDuration: 800, // Animación más suave
    };

    grafico.setOption(opcion);
  }
};
