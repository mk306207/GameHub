import {getCookie} from "./cookies.js"

document.addEventListener('DOMContentLoaded', function() {
    loadAccounts();
});
async function loadAccounts() {
    const response = await fetch('api/returnMyAccounts',{
        method:'POST',
        headers:{
            'X-CSRFToken':getCookie('csrftoken')
        },
        body:{
            'switch': "self"
        },
    });
    const data = await response.json();
    console.log(data);
    const accountList = document.getElementById("accountList")
    data.forEach(element => {
        const div = document.createElement('div');
        const gameName = document.createTextNode(element.game);
        div.appendChild(gameName);
        const spacing = document.createTextNode(" : ");
        div.appendChild(spacing);
        const accountName = document.createTextNode(element.nickname);
        div.appendChild(accountName);
        accountList.append(div)
    });
}