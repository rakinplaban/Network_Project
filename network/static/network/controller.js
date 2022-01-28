document.addEventListener("DOMContentLoaded",function(){
    document.querySelector('#like').addEventListener('click', ()=> like_function('like'));
})



let is_like = "{{is_like}}";
let num_like = "{{num_like}}";

function like_function(like){
    fetch(`/like/${posts_id}`,{
        method:"POST",
        body : JSON.stringify({
            "is_like" : is_like,
            "num_like" : num_like,
        })
    })
    .then(response => response.json())
    .then(result => {
        if(result.is_like){
            document.querySelector('#like').innerHTML = "Unike";
        }
        else{
            document.querySelector('#like').innerHTML = "Like";
        }
    })
}

// function like_function(){
//     if (document.querySelector("#like").style.color == "blue"){
//         document.querySelector("#like").style.color = "red";
//     }else{
//         document.querySelector("#like").style.color = "blue";
//     }
// }