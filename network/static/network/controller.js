document.addEventListener("DOMContentLoaded",function(){
    
    document.querySelectorAll('[id^="#likeform"]').forEach(e =>{
        e.addEventListener('submit',(event) => {
            event.preventDefault();
            like_function();
            // return false;
        });
    });
    
})



function like_function(){
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
            console.log("function is liked");
            console.log(`${result.is_like} for post ${posts_id}`);
            let num_like = result.num_like;
            console.log(`Number of posts : ${num_like}`);
            document.querySelector(`#likebtn${posts_id}`).innerHTML = "Unlike";
            num_like = num_like + 1;
            console.log(`Number of posts : ${num_like}`);
            document.querySelector(`#num_of_likes_${posts_id}`).innerHTML = `${num_like} `
            // location.replace("http://127.0.0.1:8000")
        }
        else{
            console.log("function is unliked, back off!");
            console.log(`${result.is_like} for post ${posts_id}`);
            let num_like = result.num_like;
            console.log(`Number of posts : ${num_like}`);
            document.querySelector(`#likebtn${posts_id}`).innerHTML = "Like";
            num_like = num_like - 1;
            console.log(`Number of posts : ${num_like}`);
            document.querySelector(`#num_of_likes_${posts_id}`).innerHTML = `${num_like} `
            // location.replace("http://127.0.0.1:8000")
        }
    })
    
}
