fetch("rohit.json")
.then(function(response){
    return response.json();
})
.then(function(rohit){
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let product of rohit.data){
        out +=`

        <tr>
            <td>${product.rank} </td>   
            <td>${product.name} </td>              
            <td>${product.priceUsd} </td>
            <td>${product.symbol} </td>
            <td>${product.changePercent24Hr} </td>
            <td>${product.explorer} </td>
           
        </tr>

        `;
    }

    placeholder.innerHTML=out;
})


const searchfun= () =>{
    let filter =document.getElementById("search-input");
    
    let mytable=document.getElementById("mtab");
    let tr=mytable.getElementsByTagName("tr");
    for(var i=0;i<tr.length;i++){
        let td=tr[i].getElementsByTagName("td")[0];
        if(td){
            let textvalue=td.textContent || td.innerText;
            if(textvalue.toUpperCase.indexOf(filter) > -1){
                tr[i].style.display="";         
            }else{
                tr[i].style.display= "none";
            }
        }
    }
}