document.addEventListener('DOMContentLoaded', function() {
    loadPosts();
});

async function loadPosts(){
    const response = await fetch('api/getPosts');
    const data = await response.json();
    data.reverse();
    const postsContainer = document.getElementById("postContainer_ID");
    const checks = await Promise.all(data.map(post => checkLike(post.id)));
    data.forEach((post,index)=>{
        const div = document.createElement('div');
        div.setAttribute('class','singlePost');
        const likeNum = document.createElement("P");
        likeNum.setAttribute('class','likesValue');
        likeNum.setAttribute('id', `likes_${post.id}`);
        var likesRealValue = document.createTextNode(post.score);
        likeNum.appendChild(likesRealValue);
        const a = document.createElement("A");
        a.setAttribute('class','postAuthor');
        a.setAttribute('href',`view_profile/1`);
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
        like.setAttribute('id',`likeButton_${post.id}`);
        like.addEventListener('click', function() {
            handleLike(post.id);
        });

        if (checks[index]) {
            like.style.color = "#28e01b";
        } else {
            like.style.color = "#ffffff";
        }

        div2.appendChild(like);
        p.appendChild(text);
        div.appendChild(a);
        div.appendChild(likeNum);
        div.appendChild(g);
        div.appendChild(t);
        div.appendChild(p);
        div.appendChild(div2);
        postsContainer.appendChild(div);
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
        document.getElementById(`likes_${postID}`).innerHTML = data.new_score;
        like_button = document.getElementById(`likeButton_${postID}`);
        const decision = data.liked_flag;
        console.log(decision);

        if (decision){
            like_button.style.color = "#28e01b";
            return true;
        }
        else{
            like_button.style.color = "#ffffff";
            return false;
        }
    } else {
        console.log("This so called 'engineer' sucks");
        console.log(data.error);
    }
}
async function checkLike(postID) {
    const response = await fetch('api/checkLike',{
        method:'POST',
        headers:{
            'X-CSRFToken':getCookie('csrftoken')
        },
        body: new URLSearchParams({
            'post_id':postID,
        })
        }
    )
    const data = await response.json();
    if(data.message){
        console.log(data.flag)
        return (data.flag);
    }
    else{
        console.log(data.error)
    }
}