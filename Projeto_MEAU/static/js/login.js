var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate(){
    var user = document.getElementById("username").value;
    var senha = document.getElementById("password").value;

    if (user === "operador" && senha === "1234") {
        window.location.assign ("../crud");
        return false;
    }

    else if ( (user === "funcionario" && senha === "1234") || (user === "torre" && senha === "1234") || (user === "piloto" && senha === "1234")) {
        window.location.assign ("../monitoring");
        return false;
    }

    else if (user === "gerente" && senha === "1234") {
        window.location.assign ("../reports");
        return false;
    }
    else{
        attempt --;// Decrementing by one.
        alert("Você ainda tem "+attempt+" tentativas.");
        // Disabling fields after 3 attempts.
        if( attempt == 0){
            document.getElementById("username").disabled = true;
            document.getElementById("password").disabled = true;
            document.getElementById("submit").disabled = true;
            return false;
        }
    }
}

function blockLogin(){
    document.getElementById("username").disabled = true;
    document.getElementById("password").disabled = true;
    document.getElementById("submit").disabled = true;
    return false;
}

function painel(){
    window.location.assign ("../painel");
}