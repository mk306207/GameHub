document.addEventListener('DOMContentLoaded', function() {
    loadPosts();
});

async function loadPosts(){
    const response = await fetch('api/getPosts');
    const data = await response.json();
    const postsContainer = document.getElementById("postContainer_ID");
    console.log(data)
    data.reverse().forEach(post=>{
        const div = document.createElement('div');
        div.setAttribute('class','singlePost');
        const likeNum = document.createElement("P");
        likeNum.setAttribute('class','likesValue');
        likeNum.setAttribute('id', `likes_${post.id}`);
        var likesRealValue = document.createTextNode(post.score);
        likeNum.appendChild(likesRealValue);
        const a = document.createElement("P");
        a.setAttribute('class','postAuthor');
        var titleText = document.createTextNode(post.author);
        a.appendChild(titleText);
        const g = document.createElement("P");
        g.setAttribute('class','postAuthor');
        var titleText = document.createTextNode(post.game_title);
        g.appendChild(titleText);
        const t = document.createElement("P");
        t.setAttribute('class','postTitle');
        var titleText = document.createTextNode(post.title);
        t.appendChild(titleText);
        const p = document.createElement("P");
        p.setAttribute('class','postBody');
        var text = document.createTextNode(post.text);
        const div2 = document.createElement("div");
        div2.setAttribute('class','inside');
        const like = document.createElement("A");

        like.setAttribute('class','fa-solid fa-check fa-xs likeIcon');
        like.setAttribute('id','likeButton');
        like.addEventListener('click', function() {
            handleLike(post.id);
        });
        div2.appendChild(like);
        p.appendChild(text);
        div.appendChild(a);
        div.appendChild(likeNum);
        div.appendChild(g);
        div.appendChild(t);
        div.appendChild(p);
        div.appendChild(div2);
        postsContainer.appendChild(div);
        console.log("POST ID: ",post.id," LOADED")
    })
}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue; //we return csrf token value :)
}
async function handleLike(postID){
    const response = await fetch('like_post/',{
        method:'POST',
        headers:{
            'X-CSRFToken':getCookie('csrftoken')
        },
        body: new URLSearchParams({
            'post_id':postID,
        })
    });
    const data = await response.json()
    if(data.message){
        console.log(data.message);
        document.getElementById(`likes_${postID}`).innerHTML = data.new_score;
    } else {
        console.log("This so called 'engineer' sucks");
        console.log(data.error);
    }
}