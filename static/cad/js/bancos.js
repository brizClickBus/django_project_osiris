
$(document).ready(function() {
    $("#bancosCadastrados-autocomplete").autocomplete({
        source: 'ajax-autocomplete/Bancos_cadastrados_bancoCental',
        minLength: 2
    });
});

function next(){
    location.href = "{% url 'cad_cartao' %}";
} 

// ajustar tamanaho da tbl
function mostra_oculta(id){

    var x = document.getElementById(id);
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
console.log('aa')
var tamanho = parseInt(document.getElementById("tamanhoTh").innerText)
document.getElementById("mudarTamanho").style.height=tamanho.toString()+"px"

mostra_oculta("tamanhoTh")



