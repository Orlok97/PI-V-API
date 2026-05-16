const temperatura=document.querySelector('#temperatura');
const humidade=document.querySelector('#humidade');
const qualidade_ar=document.querySelector('#qualidade_ar');

const getCurrentTemp=async ()=>{
    try{
        const response=await fetch('/api/v1/sensor/current-temp')
        if(!response.ok){
            throw new Error('erro ao buscar os dados!')
        }
        const data=await response.json()
        if(data){
            temperatura.innerHTML=`${data.temperature}°C`;
            humidade.innerHTML=`${data.humidity}%`;
        }

    }catch(err){
        console.error('Erro na requisição '+err)
    }
}

document.addEventListener("DOMContentLoaded", function() {
  getCurrentTemp();
  setInterval(getCurrentTemp, 5000);
});