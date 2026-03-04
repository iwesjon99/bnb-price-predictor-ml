async function predict(){

let open=document.getElementById("open").value
let high=document.getElementById("high").value
let low=document.getElementById("low").value
let volume=document.getElementById("volume").value

let response=await fetch("/api/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
open:open,
high:high,
low:low,
volume:volume
})

})

let data=await response.json()

document.getElementById("prediction").innerHTML=
"Predicted Price: "+data.prediction

document.getElementById("signal").innerHTML=
"Signal: "+data.decision

let ctx=document.getElementById("chart")

new Chart(ctx,{

type:"bar",

data:{
labels:["Open Price","Predicted Price"],

datasets:[{
label:"Price Comparison",
data:[open,data.prediction]
}]

}

})

}
