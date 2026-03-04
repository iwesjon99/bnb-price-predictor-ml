async function predict(){

let f1=document.getElementById("f1").value
let f2=document.getElementById("f2").value
let f3=document.getElementById("f3").value
let f4=document.getElementById("f4").value

let response=await fetch("/api/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
feature1:f1,
feature2:f2,
feature3:f3,
feature4:f4
})

})

let data=await response.json()

document.getElementById("result").innerHTML=
"Prediction: "+data.prediction+" | "+data.decision


let ctx=document.getElementById("chart")

new Chart(ctx,{
type:"line",
data:{
labels:["Prediction"],
datasets:[{
label:"Stock Value",
data:[data.prediction]
}]
}
})

}
