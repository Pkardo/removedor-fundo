function moveSlider(e) {
    const container = document.querySelector('.image-compare-container');
    const afterImage = document.getElementById('afterImage');
    const sliderBar = document.getElementById('sliderBar');

    const rect = container.getBoundingClientRect();
    let x = e.clientX - rect.left;

    x = Math.max(0, Math.min(x, rect.width));
    const percentage = (x / rect.width) * 100;

    afterImage.style.clipPath = `inset(0 ${100 - percentage}% 0 0)`;
    sliderBar.style.left = `${percentage}%`;
}
