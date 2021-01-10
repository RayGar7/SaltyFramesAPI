document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('myBtn').addEventListener('click', () => {
        document.querySelector('.bg-modal').style.display = 'flex';
    });
    document.getElementById('close').addEventListener('click',() => {
        document.querySelector('.bg-modal').style.display = 'none';
    });
});