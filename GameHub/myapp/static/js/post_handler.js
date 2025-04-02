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
        const dislike = document.createElement("A");
        dislike.setAttribute('class','fa-solid fa-xmark fa-xs dislikeIcon');
        div2.appendChild(like);
        div2.appendChild(dislike);
        p.appendChild(text);
        div.appendChild(a);
        div.appendChild(likeNum);
        div.appendChild(g);
        div.appendChild(t);
        div.appendChild(p);
        div.appendChild(div2);
        postsContainer.appendChild(div);
    })
    /*
    const div = document.createElement('div');
    div.setAttribute('class','singlePost');
    const a = document.createElement("P");
    a.setAttribute('class','postAuthor');
    var titleText = document.createTextNode("Im the author");
    a.appendChild(titleText);
    const g = document.createElement("P");
    g.setAttribute('class','postAuthor');
    var titleText = document.createTextNode("Game title");
    g.appendChild(titleText);
    const t = document.createElement("P");
    t.setAttribute('class','postTitle');
    var titleText = document.createTextNode("Hello custom title");
    t.appendChild(titleText);
    const p = document.createElement("P");
    p.setAttribute('class','postBody');
    var text = document.createTextNode("lorem dsjfdshfjksdhf");
    p.appendChild(text);
    div.appendChild(a);
    div.appendChild(g);
    div.appendChild(t);
    div.appendChild(p);
    postsContainer.appendChild(div);*/
    
}