var estilo = document.createElement("style");
estilo.setAttribute("id", "multiselect_dropdown_styles");

document.head.appendChild(estilo);

function DropdownMultiselect(opciones) {
  var configuracion = {
    altura: "15rem",
    marcador: "seleccionar",
    txtSeleccionado: " ingredientes seleccionados",
    txtTodo: "Todo",
    txtEliminar: "Eliminar",
    ...opciones,
  };

  function nuevoElemento(etiqueta, atributos) {
    var e = document.createElement(etiqueta);
    if (atributos !== undefined)
      Object.keys(atributos).forEach((k) => {
        if (k === "class") {
          Array.isArray(atributos[k])
            ? atributos[k].forEach((o) => (o !== "" ? e.classList.add(o) : 0))
            : atributos[k] !== ""
            ? e.classList.add(atributos[k])
            : 0;
        } else if (k === "style") {
          Object.keys(atributos[k]).forEach((ks) => {
            e.style[ks] = atributos[k][ks];
          });
        } else if (k === "text") {
          atributos[k] === "" ? (e.innerHTML = "&nbsp;") : (e.innerText = atributos[k]);
        } else e[k] = atributos[k];
      });
    return e;
  }

  document.querySelectorAll("select[multiple]").forEach((el) => {
    var div = nuevoElemento("div", {
      class: "multiselect-dropdown",
      style: {
        width: configuracion.style?.width ?? el.clientWidth + "px",
        padding: configuracion.style?.padding ?? "",
      },
    });
    el.style.display = "none";
    el.parentNode.insertBefore(div, el.nextSibling);
    var listaWrap = nuevoElemento("div", { class: "multiselect-dropdown-list-wrapper" });
    var lista = nuevoElemento("div", {
      class: "multiselect-dropdown-list",
      style: { height: configuracion.altura },
    });

    listaWrap.appendChild(lista);
    div.appendChild(listaWrap);

    el.cargarOpciones = () => {
      lista.innerHTML = "";

      if (el.attributes["multiselect-select-all"]?.value == "true") {
        var op = nuevoElemento("div", { class: "multiselect-dropdown-all-selector" });
        var ic = nuevoElemento("input", { type: "checkbox" });
        op.appendChild(ic);
        op.appendChild(nuevoElemento("label", { text: configuracion.txtTodo }));

        op.addEventListener("click", () => {
          op.classList.toggle("checked");
          op.querySelector("input").checked =
            !op.querySelector("input").checked;

          var ch = op.querySelector("input").checked;
          lista
            .querySelectorAll(
              ":scope > div:not(.multiselect-dropdown-all-selector)"
            )
            .forEach((i) => {
              if (i.style.display !== "none") {
                i.querySelector("input").checked = ch;
                i.optEl.selected = ch;
              }
            });

          el.dispatchEvent(new Event("change"));
        });
        ic.addEventListener("click", () => {
          ic.checked = !ic.checked;
        });

        lista.appendChild(op);
      }

      Array.from(el.options).map((o) => {
        var op = nuevoElemento("div", { class: o.selected ? "checked" : "", optEl: o });
        var ic = nuevoElemento("input", { type: "checkbox", checked: o.selected });
        op.appendChild(ic);
        op.appendChild(nuevoElemento("label", { text: o.text }));

        op.addEventListener("click", () => {
          op.classList.toggle("checked");
          op.querySelector("input").checked =
            !op.querySelector("input").checked;
          op.optEl.selected = !!!op.optEl.selected;
          el.dispatchEvent(new Event("change"));
        });
        ic.addEventListener("click", (ev) => {
          ic.checked = !ic.checked;
        });
        o.listitemEl = op;
        lista.appendChild(op);
      });
      div.listaEl = listaWrap;

      div.refrescar = () => {
        div
          .querySelectorAll("span.optext, span.placeholder")
          .forEach((t) => div.removeChild(t));
        var seleccionados = Array.from(el.selectedOptions);
        if (
          seleccionados.length > (el.attributes["multiselect-max-items"]?.value ?? 3)
        ) {
          div.appendChild(
            nuevoElemento("span", {
              class: ["optext", "maxselected"],
              text: seleccionados.length + " " + configuracion.txtSeleccionado,
            })
          );
        } else {
          seleccionados.map((x) => {
            var c = nuevoElemento("span", {
              class: "optext",
              text: x.text,
              srcOption: x,
            });
            if (el.attributes["multiselect-hide-x"]?.value !== "true")
              c.appendChild(
                nuevoElemento("span", {
                  class: "optdel",
                  text: "🗙",
                  title: configuracion.txtEliminar,
                  onclick: (ev) => {
                    c.srcOption.listitemEl.dispatchEvent(new Event("click"));
                    div.refrescar();
                    ev.stopPropagation();
                  },
                })
              );

            div.appendChild(c);
          });
        }
        if (0 == el.selectedOptions.length)
          div.appendChild(
            nuevoElemento("span", {
              class: "placeholder",
              text: el.attributes["placeholder"]?.value ?? configuracion.marcador,
            })
          );
      };
      div.refrescar();
    };
    el.cargarOpciones();

    div.addEventListener("click", () => {
      div.listaEl.style.display = "block";
    });

    document.addEventListener("click", function (event) {
      if (!div.contains(event.target)) {
        listaWrap.style.display = "none";
        div.refrescar();
      }
    });
  });
}

window.addEventListener("load", () => {
  DropdownMultiselect(window.MultiselectDropdownOptions);
});
