import {getCookie} from "./cookies.js"

document.addEventListener('DOMContentLoaded', function() {
    loadAccounts();
});
async function loadAccounts() {
    const mySwitch = document.getElementById("switch").value;
    let response;
    if (mySwitch == "other"){
        const authorID = document.getElementById("authorID").value;
        response = await fetch('api/returnMyAccounts',{
            method:'POST',
            headers:{
                'X-CSRFToken':getCookie('csrftoken')
            },
            body: new URLSearchParams({
                'switch':mySwitch,
                'authorID':authorID,
            })
        });
    }
    else{
    //     console.log("no")
     
        response = await fetch('api/returnMyAccounts',{
            method:'POST',
            headers:{
                'X-CSRFToken':getCookie('csrftoken')
            },
            body: new URLSearchParams({
                'switch':mySwitch,
            })
        });
    }
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
        console.log("Hello :)")
    });
    if(data.length == 0){
        const accountList = document.getElementById("accountList")
        const info = document.createTextNode("This user has no linked accounts");
        accountList.append(info)
    }
    
}