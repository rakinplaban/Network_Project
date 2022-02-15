document.addEventListener("DOMContentLoaded",function(){
    // const colon = document.createElement('div');
    // colon.setAttribute('id','colon')
    // e.preventDefault()
    // const likebtn = document.createElement('button');
    // likebtn.setAttribute('class','likebtn btn btn-primary');
    // likebtn.setAttribute('class','likebtn');
    // document.querySelector('.card-footer').appendChild(likebtn);
    // document.querySelector('.likebtn').innerHTML = "Like";
    
    document.querySelector(`#likebtn${posts_id}`).addEventListener('click',(event) => {
        event.preventDefault();
        like_function();
        return false;
    })
    // document.querySelector('.likepost').addEventListener('click', ()=> like_function('likepost'));
})



// let is_like = "{{is_like}}";
// let num_like = "{{num_like}}";

function like_function(){
    // document.createElement('button').innerHTML = "Love";
    // console.log("Updated!")
    fetch(`/like/${posts_id}`)
    // ,{
    //     method:"POST",
    //     body : JSON.stringify({
    //         "is_like" : is_like,
    //         "num_like" : num_like,
    //     })
    // })
    .then(response => response.json())
    .then(result => {
        if(result.is_like){
            console.log("function is liked");
            console.log(`${result.is_like} for post ${posts_id}`);
            document.querySelector(`#likebtn${posts_id}`).innerHTML = "Unike";
            // location.replace("http://127.0.0.1:8000")
        }
        else{
            console.log("function is unliked, back off!");
            console.log(`${result.is_like} for post ${posts_id}`);
            document.querySelector(`#likebtn${posts_id}`).innerHTML = "Like";
            // location.replace("http://127.0.0.1:8000")
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