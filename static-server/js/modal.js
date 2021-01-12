// js for moal functionality
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('myBtn').addEventListener('click', () => {
        document.querySelector('.bg-modal').style.display = 'flex';
        // disable scrolling on the parent too
        document.getElementById('content-head').style.overflow = 'hidden';
    });
    document.getElementById('close').addEventListener('click',() => {
        document.querySelector('.bg-modal').style.display = 'none';
        // re-enable scrolling on the parent once the modal has been closed
        document.getElementById('content-head').style.overflow = 'auto';
    });
});