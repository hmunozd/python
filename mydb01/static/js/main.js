window.onload = () => {
    let close = document.getElementsByClassName('close');
    for (let index = 0; index < close.length; index++) {
        close[index].onclick = function(){
            this.parentNode.remove();
            return false;
        }
    }
}