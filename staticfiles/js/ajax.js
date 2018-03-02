
var proceso = new Object();
proceso.tipoPro = 1;
proceso.producto = new Array();
var table = new Array();
var cliente = new Object();

$(document).ready(function(){

  $("#search-proveedores").submit(function(e){
    e.preventDefault();
    $.ajax({
      url: $(this).attr('action'),
      type: $(this).attr('method'),
      data: $(this).serialize(),
      success: function(json){
        console.log(json)
        var html = ""
        if(json.length !=0){
          for (var i = 0; i <json.length; i++) {
            html += '<tr><td>'+json[i].id+ '</td><td>'+
  						json[i].nombreEmpresa+ '</td><td>'+
  						json[i].nombreRepresentante+'</td></tr>'
          }
          $("#datosC").html(html);
        }
        else {
          var msg = 'No existe provedores relacionados con el dato.'
          alert(msg);
        }
      }
    })
  })

  $('#c-buscar').submit(function(e){
    e.preventDefault();
    $.ajax({
      url: $(this).attr('action'),
      type: $(this).attr('method'),
      data: $(this).serialize(),
      success: function(json){
        console.log(json)
        var html = ""
        if (json.length != 0) {
          for (var i = 0; i < json.length; i++) {
            html += 'DNI: '+json[i].dni + '<br>';
            html += 'Empresa: '+json[i].nombreEmpresa + '<br>';
            html += 'Nombres: '+json[i].nombreRepresentante + '<br>';
            html += 'Apellidos: '+json[i].apellidoRepresentante + '<hr>';

            cliente.dni = json[i].dni;
            cliente.nombreEmpresa = json[i].nombreEmpresa;
            cliente.nombreRepresentante = json[i].nombreRepresentante;
            cliente.apellidoRepresentante = json[i].apellidoRepresentante;
          }
          $('#clientes').html(html);
          $("#c-seleccionar").attr("disabled", false);
        }else{
          html += '<strong>No existe Cliente con ese numero de identificación</strong><br>';
          $('#clientes').html(html);
          $("#c-seleccionar").attr("disabled", true);
        }

      }
    })
  })

$("#c-seleccionar").click(function(){
  proceso.clienProv = cliente.dni;
  $("#c-dni").text(cliente.dni);
  $("#c-nombreEmpresa").text(cliente.nombreEmpresa);
  $("#c-nombreRepresentante").text(cliente.nombreRepresentante);
  $("#c-apellidoRepresentante").text(cliente.apellidoRepresentante);

  if (proceso.clienProv.length != 0){
    var htm = ""
    $('#clientes').html(htm);
    $("#idusuario").val('');
    $("#c-seleccionar").attr("disabled", true);
  }
})


/*productos ajax*/
$('#p-buscar').submit(function(e){
  e.preventDefault();
  $.ajax({
    url: $(this).attr('action'),
    type: $(this).attr('method'),
    data: $(this).serialize(),
    success: function(json){
      // console.log(JSON.stringify(json))
      var html = ""
      if (json.length !=0) {


      for (var i = 0; i < json.length; i++) {
        html += 'Codigo: '+json[i].fields.codigo + '<br>';
        html += 'Producto: '+json[i].fields.producto + '<br>';
        html += '<label> Valor venta: </label> <input name="p-valorVenta" id="p-valorVenta" type="number" min="1" max="50000000" step="500" value="'+json[i].fields.valorVenta+'" autocomplete="off" required="required"><br>';
        html += '<label> Cantidad: </label> <input name="p-cantidad" id="p-cantidad" type="number" min="1" max="200" step="1" value=1 autocomplete="off" required="required"><br>';
        html += '<select id="list_precio" onchange="selectPecio();"> <option value="'+json[i].fields.valorVenta+'"> Consumo paquete </option> <option value="'+json[i].fields.valorDP+'"> Distribuidor paquete </option> <option value="'+json[i].fields.valorDC+'"> Distribuidor caja </option><option value="'+json[i].fields.valorCC+'"> Consumo caja </option></select><hr>';

        var fila = new Object();
        fila.codigo = json[i].fields.codigo;
        fila.producto = json[i].fields.producto;
        fila.valorIva = 0.19;
        /*fila.valorVenta = json[i].fields.valorVenta;*/
        fila.cantidad = 1;
        // fila.valorVenta = 1;
        table.push(fila);
      }
      $("#p-seleccionar").attr("disabled", false);
      $('#productos').html(html);
    }else{
      html += '<strong>No existe Medicamento con ese code</strong><br>';
      $('#productos').html(html);
      $("#p-seleccionar").attr("disabled", true);
    }
    }
  })
})

$("#p-seleccionar").click(function(){
  var d = table;
  var t = document.getElementById('tb-detalle').getElementsByTagName('tbody')[0];
  var rowCount = t.rows.length;
  var row = t.insertRow(rowCount);
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);
  var cell4 = row.insertCell(3);
  var cell5 = row.insertCell(4);
  var cell6 = row.insertCell(5);
  var cell7 = row.insertCell(6);

  cell1.innerHTML = d[d.length-1].codigo;
  cell2.innerHTML = d[d.length-1].producto;
  d[d.length-1].valorVenta = $('#p-valorVenta').val();
  cell3.innerHTML = d[d.length-1].valorVenta-(d[d.length-1].valorVenta * d[d.length-1].valorIva);
  d[d.length-1].cantidad = $('#p-cantidad').val();
  cell4.innerHTML = d[d.length-1].cantidad;
  cell5.innerHTML = (d[d.length-1].valorVenta * d[d.length-1].valorIva) * $('#p-cantidad').val();
  cell6.innerHTML = d[d.length-1].valorVenta  * $('#p-cantidad').val() ;
  cell7.innerHTML = '<td><input type="button" class="borrar" value="Eliminar" /></td>';
  cell1.setAttribute('align','center');
  cell2.setAttribute('align','center');
  cell3.setAttribute('align','center');
  cell4.setAttribute('align','center');
  cell5.setAttribute('align','center');
  cell6.setAttribute('align','center');

  proceso.producto.push({'codigo': d[d.length-1].codigo, 'cantidad': d[d.length-1].cantidad, 'valorVenta': d[d.length-1].valorVenta});
  calTotal();
  vueltas();
  var efectivo = $("#efectivo").val();
  var valor = verificar("p-total");
  vueltas();
  if (proceso.producto.length !=0){
    var htm = ""
    $('#productos').html(htm);
    $("#pcodigo").val('');
    $("#p-seleccionar").attr("disabled", true);

    if (efectivo>=valor) {
      $("#comprar").attr("disabled", false);
    }
  }

})

})//principal

//funciones aparte

function onEnviar(){
    //proceso.serie = $('#p-serie').val();
    //proceso.numero = $('#p-num').val();
    var tipoPago = $("#f-tipoPago").val();
    var idMaquina = $("#f-maquinaid").val();
    var efectivo = $("#efectivo").val();
    var devolver = $("#devolver").val();
    proceso.tipoPago = tipoPago;
    proceso.idMaquina = idMaquina;
    proceso.efectivo = efectivo;
    proceso.devolver = devolver;

    console.log(JSON.stringify(proceso));
    document.getElementById("proceso").value=JSON.stringify(proceso);
}

var total = 0;
function calTotal(){
    var total=0;
    var t=0;
    $('#tb-detalle tbody tr').each(function () {
      console.log(total);
        total = total*1 + $(this).find("td").eq(5).html()*1;
        console.log(total);
        t = t*1 + $(this).find("td").eq(4).html()*1;

    });
    $('#p-subtotal').text((total-t));
    $('#p-iva').text(t.toFixed(2));
    // $('#p-total').text(total);
    document.getElementById("p-total").value= total;

}

function selectPecio(){
  var selectedValue = document.getElementById("list_precio").value;
  /*console.log(selectedValue);
  alert("valor: "+selectedValue);*/
  document.getElementById("p-valorVenta").value=selectedValue;
}


$(document).on('click', '.borrar', function (event) {
     event.preventDefault();
     $(this).closest('tr').remove();
     calTotal();
     vueltas();
});


 function vueltas() {
     var iva=0.19
     var valor = verificar("p-total");
     var efectivo=verificar("efectivo");
     // realizamos la suma de los valores y los ponemos en la casilla del
     // formulario que contiene el total o-subtotal

     var devolver = efectivo - valor;


     if (devolver < 0) {
       document.getElementById("devolver").value= "Faltan $"+ Math.abs(devolver);
       $('#comprar').attr('disabled',true);
     }
     else {
       document.getElementById("devolver").value= devolver;
       $('#comprar').attr('disabled',false);
     }
 }
 /**
  * Funcion para verificar los valores de los cuadros de texto. Si no es un
  * valor numerico, cambia de color el borde del cuadro de texto
  */
 function verificar(id)
 {
     var obj=document.getElementById(id);
     if(obj.value=="")
         value="0";
     else
         value=obj.value;
     if(validate_importe(value,1))
     {
         // marcamos como erroneo
         obj.style.borderColor="#808080";
         return value;
     }else{
         // marcamos como erroneo
         obj.style.borderColor="#f00";
         return 0;
     }
 }
 /**
  * Funcion para validar el importe
  * Tiene que recibir:
  *  El valor del importe (Ej. document.formName.operator)
  *  Determina si permite o no decimales [1-si|0-no]
  * Devuelve:
  *  true-Todo correcto
  *  false-Incorrecto
  */
 function validate_importe(value,decimal)
 {
     if(decimal==undefined)
         decimal=0;
     if(decimal==1)
     {
         // Permite decimales tanto por . como por ,
         var patron=new RegExp("^[0-9]+((,|\.)[0-9]{1,2})?$");
     }else{
         // Numero entero normal
         var patron=new RegExp("^([0-9])*$")
     }
     if(value && value.search(patron)==0)
     {
         return true;
     }
     return false;
 }
