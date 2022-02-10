document.addEventListener("DOMContentLoaded",function(e){
    // const colon = document.createElement('div');
    // colon.setAttribute('id','colon')
    e.preventDefault()
    document.querySelector('.likepost').addEventListener('click', ()=> like_function('likepost'));
})



// let is_like = "{{is_like}}";
// let num_like = "{{num_like}}";

function like_function(likepost){
    document.createElement('button').innerHTML = "Love";
    fetch(`/likepost/${posts_id}`)
    // ,{
    //     method:"POST",
    //     body : JSON.stringify({
    //         "is_like" : is_like,
    //         "num_like" : num_like,
    //     })
    // })
    .then(response => response.json())
    .then(result => {
        console.log("Updated.");
        if(result.is_like){
            document.querySelector('#like').innerHTML = "Unike";
        }
        else{
            document.querySelector('#like').innerHTML = "Like";
        }
    })
    location.replace("http://127.0.0.1/")
}

// function like_function(){
//     if (document.querySelector("#like").style.color == "blue"){
//         document.querySelector("#like").style.color = "red";
//     }else{
//         document.querySelector("#like").style.color = "blue";
//     }
// }