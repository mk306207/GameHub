document.addEventListener('DOMContentLoaded', function() {
    loadAccounts();
});
async function loadAccounts() {
    const response = await fetch('api/returnMyAccounts');
    const data = await response.json();
    console.log(data);
}